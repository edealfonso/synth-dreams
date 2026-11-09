from django.urls import path

from .views import HomeView, LegalPageView

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('legal/<str:slug>', LegalPageView.as_view(), name="legal"),
]
