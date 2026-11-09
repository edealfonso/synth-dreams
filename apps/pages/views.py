from django.views.generic import TemplateView, DetailView

from apps.galleries.models import FirstGalleryImage, SecondGalleryImage

from .models import Home, Vignette, MagnifyItem, LegalPage


class HomeView(TemplateView):
    """One-page home: everything the template needs goes into the context."""

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['home'] = Home.objects.first()

        context['vignettes_1'] = Vignette.objects.filter(group=1)
        context['vignettes_2'] = Vignette.objects.filter(group=2)
        context['vignettes_3'] = Vignette.objects.filter(group=3)
        context['magnify_items'] = MagnifyItem.objects.all()

        context['gallery_1'] = FirstGalleryImage.objects.all()
        context['gallery_2'] = SecondGalleryImage.objects.all()

        return context


class LegalPageView(DetailView):
    template_name = 'legal.html'
    model = LegalPage
    slug_url_kwarg = 'slug'
    context_object_name = 'page'
