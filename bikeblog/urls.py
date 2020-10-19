from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import BikeBlogView, BikeDetailView, AddBikeBlogView, UpdateBlogView, DeleteBlogView

urlpatterns = [

    path('bikeblog/', BikeBlogView.as_view(), name="bikeblog"),
    path('blog_detail/<int:pk>/', BikeDetailView.as_view(), name="blog_detail"),
    path('add_blog/', AddBikeBlogView.as_view(), name="add_blog"),
    path('blog_detail/edit/<int:pk>/', UpdateBlogView.as_view(), name="edit_blog"),
    path('blog_detail/<int:pk>/delete', DeleteBlogView.as_view(), name="delete_blog"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
