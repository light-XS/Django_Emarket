from django.urls import path
from . import views
urlpatterns = [
    path("get_all_product", views.get_all_product,name ='get_all_product'),
    path("get_filterd_products", views.get_product_filtered,name ='get_filterd_products'),
    path("get_one_product/<int:pk>", views.get_one_product,name ='get_one_product'),
]
