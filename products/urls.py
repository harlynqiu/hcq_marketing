from django.urls import path
from . import views

urlpatterns = [
    path('products/index', views.index, name='products_index'),  # Home page that lists products
    path('products/<int:id>/', views.view_product, name='view_product'),  # View individual customers
    path('products/add/', views.add, name='add_product'),  # Route to add customers
]