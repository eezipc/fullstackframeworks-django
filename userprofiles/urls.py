from django.urls import path
from . import views

urlpatterns = [
    path('', views.userprofileview, name='userprofileview')
]