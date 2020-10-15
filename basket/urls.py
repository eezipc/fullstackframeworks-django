"""eezimotorcycles URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.basketview, name='basketview'),
    path('updatebasket/<item_id>', views.updatebasketview,
         name='updatebasketview'),
    path('changebasket/<item_id>', views.changebasketview,
         name='changebasketview'),
    path('deletebasket/<item_id>', views.deletebasketview,
         name='deletebasketview'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
