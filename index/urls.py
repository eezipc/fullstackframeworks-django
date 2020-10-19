"""eezimotorcycles URL Configuration

"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ContactCreate
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("contact/", ContactCreate.as_view(), name="contact"),
    path("thanks/", views.thanks, name="thanks"),
    path('terms', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),
    path('success', views.success, name='success'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
