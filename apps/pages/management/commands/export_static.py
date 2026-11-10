"""Static export of the public site (home and legal pages, ES and EN) for GitHub Pages.

Renders every page through the test client and writes plain HTML files, then copies the static
files and the media files the pages use. The admin is never exported.

Run it with the same SITE_PREFIX the webpack build used, e.g. for GitHub Pages:

    SITE_PREFIX=/synth-dreams npm run build
    SITE_PREFIX=/synth-dreams python manage.py export_static

URLs map to files the way GitHub Pages serves them: `/` and `/en/` -> `index.html` in their
folder, `/legal/<slug>` -> `legal/<slug>.html`.
"""
import re
import shutil
from pathlib import Path
from urllib.parse import unquote

from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.management.base import BaseCommand, CommandError
from django.test import Client
from django.urls import reverse
from django.utils import translation

from apps.pages.models import LegalPage

# static folders copied whole: CSS assets (fonts) and files referenced from JS or the web manifest
STATIC_DIRS = ('bundles', 'favicon', 'img')


class Command(BaseCommand):
    help = "Export the public pages as a static site (default folder: dist/)."

    def add_arguments(self, parser):
        parser.add_argument('--output', default=str(Path(settings.BASE_DIR) / 'dist'),
                            help="Output folder (wiped first).")

    def handle(self, *args, **options):
        out = Path(options['output'])
        prefix = (settings.FORCE_SCRIPT_NAME or '').rstrip('/')
        static_url = settings.STATIC_URL  # already prefixed by Django when relative
        media_url = settings.MEDIA_URL

        if out.exists():
            shutil.rmtree(out)
        out.mkdir(parents=True)

        client = Client(HTTP_HOST='localhost')
        referenced = set()

        for url in self.page_urls():
            path_info = url[len(prefix):] if prefix and url.startswith(prefix) else url
            response = client.get(path_info)
            if response.status_code != 200:
                raise CommandError(f"{url} returned {response.status_code}")
            html = response.content.decode('utf-8')
            referenced |= self.local_urls(html, static_url, media_url)

            target = out / (path_info.lstrip('/') + 'index.html' if path_info.endswith('/')
                            else path_info.lstrip('/') + '.html')
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(html, encoding='utf-8')
            self.stdout.write(f"page  {url} -> {target.relative_to(out)}")

        static_root = out / 'static'
        for folder in STATIC_DIRS:
            source = finders.find(folder)
            if not source:
                raise CommandError(f"Static folder '{folder}' not found (run the webpack build first)")
            shutil.copytree(source, static_root / folder, dirs_exist_ok=True)

        copied = 0
        for url in sorted(referenced):
            if url.startswith(static_url):
                rel = unquote(url[len(static_url):])
                source = finders.find(rel)
                target = static_root / rel
            else:
                rel = unquote(url[len(media_url):])
                source = Path(settings.MEDIA_ROOT) / rel
                target = out / 'media' / rel
                if not source.is_file():
                    source = None
            if not source:
                raise CommandError(f"Referenced file not found: {url}")
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            copied += 1

        # no Jekyll processing on GitHub Pages
        (out / '.nojekyll').touch()

        size = sum(f.stat().st_size for f in out.rglob('*') if f.is_file()) / 1e6
        self.stdout.write(self.style.SUCCESS(
            f"Exported to {out} ({copied} referenced files + {', '.join(STATIC_DIRS)}; {size:.1f} MB)."))

    def page_urls(self):
        urls = []
        for code, _name in settings.LANGUAGES:
            with translation.override(code):
                urls.append(reverse('pages:home'))
                urls += [reverse('pages:legal', kwargs={'slug': page.slug})
                         for page in LegalPage.objects.all()]
        return urls

    @staticmethod
    def local_urls(html, static_url, media_url):
        """Static and media URLs used by a page (attributes, inline styles, data-src…)."""
        pattern = r'(?:%s|%s)[^"\'()\s<>]+' % (re.escape(static_url), re.escape(media_url))
        return {url for url in re.findall(pattern, html)}
