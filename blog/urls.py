from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('deposit',views.deposit, name='deposit_list')
]