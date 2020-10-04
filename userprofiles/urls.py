from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile_order_history/<orderid>', views.profile_order_history, name='profile_order_history'),

]