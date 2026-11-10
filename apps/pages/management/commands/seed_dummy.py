"""
Placeholder content to see the site working locally.

Fills Header, Home, Footer, vignettes, magnify items, legal pages and both galleries with silly text
(ES and EN) and images generated with Pillow. Each image shows the name of its field, so you
can tell what every one of them renders on the page.

Usage:
    python manage.py seed_dummy                   # fill (deletes previous content first)
    python manage.py seed_dummy --video path.mp4  # also use that video for the video fields

Temporary: phase 5 replaces it with the real content (seed_demo).
"""

import colorsys
import io
import shutil
import zlib

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from PIL import Image, ImageDraw, ImageFont

from apps.galleries.models import FirstGalleryImage, SecondGalleryImage
from apps.pages.models import Footer, Header, Home, LegalPage, Vignette, MagnifyItem

LANDSCAPE = (1920, 1200)
PORTRAIT = (900, 1600)
SQUARE = (1000, 1000)
SMALL = (600, 600)
LOGO = (900, 300)

# Spanish is the default language of the site; each text has its English version
PARAGRAPH = (
    '<p>Bip bup, esto es texto de relleno. Las máquinas hacen ruiditos, '
    'los botones son grandes y los colores no tienen miedo.</p>',
    '<p>Beep boop, this is placeholder text. Machines make little noises, '
    'buttons are big and colours are fearless.</p>',
)
LONG_PARAGRAPH = (
    PARAGRAPH[0] + '<p>Otro párrafo tonto para ver cómo se comporta el texto cuando ocupa más líneas. '
    'Perillas, pads, teclas, cables y un poco de cinta americana.</p>',
    PARAGRAPH[1] + '<p>Another silly paragraph to see how text behaves when it takes more lines. '
    'Knobs, pads, keys, cables and a bit of duct tape.</p>',
)


def placeholder_image(label, size=LANDSCAPE, transparent=False):
    """PNG with a colour gradient (stable for each label) and the label written in the middle."""
    width, height = size
    hue = (zlib.crc32(label.encode()) % 360) / 360

    if transparent:
        img = Image.new('RGBA', size, (0, 0, 0, 0))
    else:
        c1 = tuple(int(v * 255) for v in colorsys.hsv_to_rgb(hue, 0.65, 0.95))
        c2 = tuple(int(v * 255) for v in colorsys.hsv_to_rgb((hue + 0.15) % 1, 0.75, 0.6))
        # vertical gradient: build a single column and stretch it
        column = Image.new('RGB', (1, height))
        for y in range(height):
            t = y / max(height - 1, 1)
            column.putpixel((0, y), tuple(int(a + (b - a) * t) for a, b in zip(c1, c2)))
        img = column.resize(size)

    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default(size=max(24, min(width, height) // 12))
    text = f'{label}\n{width}x{height}'
    box = draw.multiline_textbbox((0, 0), text, font=font, align='center')
    pos = ((width - (box[2] - box[0])) / 2, (height - (box[3] - box[1])) / 2)
    colour = (30, 30, 30, 255) if transparent else (255, 255, 255)
    draw.multiline_text(pos, text, font=font, fill=colour, align='center')

    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    return ContentFile(buffer.getvalue(), name=f'dummy/{label}.png')


def set_translated(obj, field, es, en=None):
    """Fill a translatable field in both languages."""
    setattr(obj, f'{field}_es', es)
    setattr(obj, f'{field}_en', en if en is not None else es)


def set_file(obj, field, content):
    getattr(obj, field).save(content.name, content, save=False)


def tagged(field, html):
    """Prefix the first paragraph with the field name, so it is easy to spot on the page."""
    return html.replace('<p>', f'<p><strong>[{field}]</strong> ', 1)


class Command(BaseCommand):
    help = 'Fill the database with placeholder content (silly text and generated images).'

    def add_arguments(self, parser):
        parser.add_argument('--video', help='Path to an .mp4 for the video fields (optional).')

    def handle(self, *args, **options):
        # empty media/dummy so copies do not pile up when the command is run again
        for folder in ('dummy', 'video/dummy'):
            shutil.rmtree(settings.MEDIA_ROOT.child(*folder.split('/')), ignore_errors=True)
        for model in (Vignette, MagnifyItem, LegalPage, FirstGalleryImage, SecondGalleryImage):
            model.objects.all().delete()

        video = None
        if options['video']:
            with open(options['video'], 'rb') as f:
                video = f.read()

        self.header()
        self.home(video)
        self.vignettes()
        self.magnify_items()
        self.galleries()
        self.footer()
        self.legal_pages()

        self.stdout.write(self.style.SUCCESS('Placeholder content created.'))
        if not video:
            self.stdout.write('No video: pass --video path.mp4 to try the lazy-loaded videos.')

    # ------------------------------------------------------------

    def header(self):
        h = Header.get_solo()
        set_file(h, 'logo', placeholder_image('header-logo', LOGO, transparent=True))
        set_translated(h, 'contact_link_text', 'Contacto', 'Contact')
        h.language_selector_es = 'ES'
        h.language_selector_en = 'EN'
        h.save()

    def home(self, video):
        h = Home.get_solo()

        # images: one per field, with its name written on it
        images = {
            's01_logo': (LOGO, True),
            's01_image': (LANDSCAPE, False),
            's01_image_mobile': (PORTRAIT, False),
            's02_image': (LANDSCAPE, False),
            's04_video_poster': (LANDSCAPE, False),
            's05_image': (LANDSCAPE, False),
            's08_image1': (LANDSCAPE, False),
            's08_image1_mobile': (PORTRAIT, False),
            's08_image2': (LANDSCAPE, False),
            's08_image2_mobile': (PORTRAIT, False),
            's09_left_image': (PORTRAIT, False),
            's10_image': (LANDSCAPE, False),
            's10_video_poster': (LANDSCAPE, False),
            's11_image': (LANDSCAPE, False),
            's13_image': (SQUARE, False),
            's14_image': (LANDSCAPE, False),
            's15_image_left': (LANDSCAPE, False),
            's15_image_right': (LANDSCAPE, False),
            's16_image': (SQUARE, False),
            's17_image': (LANDSCAPE, False),
        }
        for field, (size, transparent) in images.items():
            set_file(h, field, placeholder_image(field, size, transparent))

        if video:
            for field in ('s04_video_high', 's04_video_low', 's10_video_high', 's10_video_low'):
                getattr(h, field).save(f'dummy/{field}.mp4', ContentFile(video), save=False)

        # titles: (es, en), following the proposed Synth Dreams structure
        titles = {
            's02_title': ('Máquinas que hacen sonreír', 'Machines that make you smile'),
            's06_step_title1': ('Cajas de ritmos', 'Drum machines'),
            's06_step_title2': ('Sintetizadores', 'Synthesizers'),
            's06_step_title3': ('Cacharros', 'Gadgets'),
            's07_title': ('Galería 1', 'Gallery 1'),
            's08_title': ('Teclas y perillas', 'Keys and knobs'),
            's09_title': ('Anatomía de un sinte', 'Anatomy of a synth'),
            's09_group_title1': ('Oscilador: título del grupo 1', 'Oscillator: group title 1'),
            's09_group_title2': ('Filtro: título del grupo 2', 'Filter: group title 2'),
            's09_group_title3': ('Envolvente: título del grupo 3', 'Envelope: group title 3'),
            's10_title': ('Del circuito al sonido', 'From circuit to sound'),
            's11_title': ('Máquina icónica', 'Iconic machine'),
            's12_title': ('Galería 2', 'Gallery 2'),
            's13_title': ('Pequeños estudios caseros', 'Tiny home studios'),
            's15_title_line1': ('Beep', 'Beep'),
            's15_title_line2': ('Boop', 'Boop'),
            's16_title': ('Empieza hoy', 'Start today'),
            's16_point_title1': ('Elige una máquina', 'Pick a machine'),
            's16_point_title2': ('Conéctala', 'Plug it in'),
            's16_point_title3': ('Graba', 'Record'),
        }
        for field, (es, en) in titles.items():
            set_translated(h, field, es, en)

        # rich texts: every one starts with its field name
        texts = {
            's02_text': PARAGRAPH,
            's03_text': PARAGRAPH,
            's05_text': (
                '<p>Tres formas de hacer ruido (statement de la sección 1).</p>',
                '<p>Three ways to make noise (section 1 statement).</p>',
            ),
            's06_step_text1': PARAGRAPH,
            's06_step_text2': PARAGRAPH,
            's06_step_text3': PARAGRAPH,
            's07_text': PARAGRAPH,
            's08_text': LONG_PARAGRAPH,
            's09_text': PARAGRAPH,
            's10_text': PARAGRAPH,
            's11_text': LONG_PARAGRAPH,
            's12_text': PARAGRAPH,
            's13_text': PARAGRAPH,
            's14_text': PARAGRAPH,
            's15_text': PARAGRAPH,
            's16_text': PARAGRAPH,
            's16_point_text1': PARAGRAPH,
            's16_point_text2': PARAGRAPH,
            's16_point_text3': PARAGRAPH,
            's17_text': (
                '<p>Frase final de relleno: apaga el ordenador y enciende una caja de ritmos.</p>',
                '<p>Placeholder closing line: switch off the computer and switch on a drum machine.</p>',
            ),
        }
        for field, (es, en) in texts.items():
            set_translated(h, field, tagged(field, es), tagged(field, en))

        h.save()

    def vignettes(self):
        # group 1: three floating images (#s09-floating-0..2)
        # group 2: square and round; group 3: three texts of the effect chain (see home.html)
        rows = [
            ('1', 'FLOATING'), ('1', 'FLOATING'), ('1', 'FLOATING'),
            ('2', 'SQUARE'), ('2', 'ROUND'), ('2', 'ROUND'),
            ('3', 'CHAIN'), ('3', 'CHAIN'), ('3', 'CHAIN'),
        ]
        for i, (group, kind) in enumerate(rows):
            vignette = Vignette(group=group, kind=kind, the_order=i)
            if kind != 'CHAIN':
                set_file(vignette, 'image', placeholder_image(f'vignette-{group}-{i}-{kind.lower()}', SMALL))
            for n in (1, 2, 3):
                set_translated(
                    vignette, f'text{n}',
                    f'<p>Texto {n} de la viñeta {i}: perilla, pad o tecla.</p>',
                    f'<p>Text {n} of vignette {i}: knob, pad or key.</p>',
                )
            vignette.save()

    def magnify_items(self):
        rules = [
            ('Juega primero', 'Play first'),
            ('Botones grandes', 'Big buttons'),
            ('Colores sin miedo', 'Fearless colours'),
            ('Nada de manuales', 'No manuals'),
            ('Ruido con gracia', 'Noise with charm'),
        ]
        for i, (es, en) in enumerate(rules):
            item = MagnifyItem(the_order=i)
            set_translated(item, 'title', es, en)
            set_translated(item, 'text', *PARAGRAPH)
            item.save()

    def galleries(self):
        # the desktop animations expect 4 images per gallery (#s07-pair-0/2, #s12-pair-0/2)
        for model, name in ((FirstGalleryImage, 'gallery1'), (SecondGalleryImage, 'gallery2')):
            for i in range(4):
                obj = model(the_order=i)
                set_file(obj, 'image', placeholder_image(f'{name}-{i}', PORTRAIT if i % 2 else LANDSCAPE))
                obj.save()

    def footer(self):
        f = Footer.get_solo()
        set_translated(f, 'text', *PARAGRAPH)
        set_translated(f, 'map_link_text', 'Ver mapa', 'See map')
        set_translated(f, 'contact_details', '<p>Calle del Ruido, 1<br>hola@example.com</p>',
                       '<p>1 Noise Street<br>hello@example.com</p>')
        f.github = 'https://example.com/github'
        f.linkedin = 'https://example.com/linkedin'
        f.youtube = 'https://example.com/youtube'
        set_file(f, 'map', placeholder_image('footer-map', LANDSCAPE))
        set_file(f, 'bottom_image', placeholder_image('footer-bottom-image', LANDSCAPE))
        f.copyright = 'Elsa de Alfonso'
        f.save()

    def legal_pages(self):
        for i, (es, en) in enumerate((('Aviso legal', 'Legal notice'), ('Cookies', 'Cookies'))):
            page = LegalPage(the_order=i)
            set_translated(page, 'title', es, en)
            set_translated(page, 'content', *LONG_PARAGRAPH)
            page.save()
