from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.allshopitems, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('new_product/', views.new_product, name='new_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)