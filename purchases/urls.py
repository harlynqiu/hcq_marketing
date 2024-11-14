from django.urls import path
from . import views

urlpatterns = [
    path('', views.purchase_index, name='purchase_index'),
    path('add/', views.purchase_add, name='purchase_add'),
]
