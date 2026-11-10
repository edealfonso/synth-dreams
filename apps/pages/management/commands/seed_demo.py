"""
Real Synth Dreams content, loaded from the seed/ directory.

seed/content.json holds every row of the home models (texts in ES and EN, image paths) and
seed/images/ (or any other folder in seed/, except backup/ and texts/) holds the files. Image
paths in content.json are relative to seed/.

Usage:
    python manage.py seed_demo           # wipe the content and load it from seed/ (fresh clone, CI)
    python manage.py seed_demo --export  # write the current database back to seed/content.json

Loading copies the files into media/demo/ and rewrites the paths, so the admin keeps working.
Exporting matches every file in media/ with its copy in seed/ by content (any name); a file with
no copy is added to seed/images/ under its own name. Placeholder files (under a dummy/ folder)
are not exported: the field is left empty. Sortable rows get consecutive the_order values.
"""

import hashlib
import json
import os
import shutil

from django.conf import settings
from django.core import serializers
from django.core.management.base import BaseCommand, CommandError
from django.db import models, transaction

from apps.galleries.models import FirstGalleryImage, SecondGalleryImage
from apps.pages.models import Footer, Header, Home, LegalPage, MagnifyItem, Vignette

SEED_DIR = settings.BASE_DIR.child('seed')
CONTENT_FILE = SEED_DIR.child('content.json')
SEED_IGNORE = {'backup', 'texts'}
MEDIA_SUBDIR = 'demo'

SINGLETONS = (Header, Home, Footer)
SORTABLES = (Vignette, MagnifyItem, LegalPage, FirstGalleryImage, SecondGalleryImage)
MODELS = SINGLETONS + SORTABLES


def file_fields(model):
    return [f.name for f in model._meta.fields if isinstance(f, models.FileField)]


def md5(path):
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def seed_files():
    """{md5: path relative to seed/} for every file in seed/ except backup/ and texts/."""
    found = {}
    for root, dirs, files in os.walk(SEED_DIR):
        rel_root = os.path.relpath(root, SEED_DIR)
        if rel_root.split(os.sep)[0] in SEED_IGNORE:
            dirs[:] = []
            continue
        for name in sorted(files):
            if name.startswith('.') or name == 'content.json' or name.endswith('.md'):
                continue
            path = os.path.join(root, name)
            found.setdefault(md5(path), os.path.relpath(path, SEED_DIR))
    return found


class Command(BaseCommand):
    help = 'Load the real content from seed/ (or write the database back to it with --export).'

    def add_arguments(self, parser):
        parser.add_argument('--export', action='store_true',
                            help='Write the current database to seed/content.json instead of loading it.')

    def handle(self, *args, **options):
        if options['export']:
            self.export()
        else:
            self.load()

    # ------------------------------------------------------------

    def export(self):
        known = seed_files()
        rows = []
        for model in MODELS:
            fields = file_fields(model)
            queryset = model.objects.all()
            if model in SORTABLES:
                queryset = queryset.order_by('the_order', 'pk')
            for order, obj in enumerate(queryset, start=1):
                row = json.loads(serializers.serialize('json', [obj]))[0]
                row.pop('pk')
                if model in SORTABLES:
                    row['fields']['the_order'] = order
                for field in fields:
                    row['fields'][field] = self.export_file(getattr(obj, field).name, known)
                rows.append(row)

        with open(CONTENT_FILE, 'w', encoding='utf-8') as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)
            f.write('\n')
        self.stdout.write(self.style.SUCCESS(f'Exported {len(rows)} rows to seed/content.json.'))

    def export_file(self, name, known):
        """Path relative to seed/ for a media file ('' when empty or placeholder)."""
        if not name:
            return ''
        if 'dummy/' in name:
            self.stdout.write(f'  skipped placeholder: {name}')
            return ''
        source = settings.MEDIA_ROOT.child(*name.split('/'))
        if not os.path.exists(source):
            raise CommandError(f'Missing media file: {name}')
        digest = md5(source)
        if digest not in known:
            target = os.path.join('images', os.path.basename(name))
            if os.path.exists(SEED_DIR.child(*target.split('/'))):
                raise CommandError(f'{target} already exists in seed/ with other content ({name}).')
            shutil.copyfile(source, SEED_DIR.child(*target.split('/')))
            known[digest] = target
            self.stdout.write(f'  added to seed/: {target}')
        return known[digest].replace(os.sep, '/')

    # ------------------------------------------------------------

    @transaction.atomic
    def load(self):
        if not os.path.exists(CONTENT_FILE):
            raise CommandError('seed/content.json not found.')
        with open(CONTENT_FILE, encoding='utf-8') as f:
            rows = json.load(f)

        media_dir = settings.MEDIA_ROOT.child(MEDIA_SUBDIR)
        shutil.rmtree(media_dir, ignore_errors=True)
        for model in SORTABLES:
            model.objects.all().delete()

        by_label = {model._meta.label_lower: model for model in MODELS}
        for row in rows:
            model = by_label.get(row['model'])
            if model is None:
                raise CommandError(f'Unknown model in content.json: {row["model"]}')
            fields = dict(row['fields'])
            for field in file_fields(model):
                fields[field] = self.load_file(fields.get(field) or '')
            row = {'model': row['model'], 'fields': fields}
            if model in SINGLETONS:
                row['pk'] = model.singleton_instance_id
            for obj in serializers.deserialize('json', json.dumps([row])):
                obj.save()

        self.stdout.write(self.style.SUCCESS(f'Loaded {len(rows)} rows from seed/content.json.'))

    def load_file(self, rel_path):
        """Copy seed/<rel_path> into media/demo/ and return its media name."""
        if not rel_path:
            return ''
        source = SEED_DIR.child(*rel_path.split('/'))
        if not os.path.exists(source):
            raise CommandError(f'Missing seed file: seed/{rel_path}')
        target = settings.MEDIA_ROOT.child(MEDIA_SUBDIR, *rel_path.split('/'))
        os.makedirs(os.path.dirname(target), exist_ok=True)
        shutil.copyfile(source, target)
        return f'{MEDIA_SUBDIR}/{rel_path}'
