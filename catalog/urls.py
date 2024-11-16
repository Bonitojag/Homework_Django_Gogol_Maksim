from django.urls import path
from catalog.views import home, product_detail, contact, category_products, create_product

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('contacts/', contact, name='contact'),
    path('category/<int:category_id>/', category_products, name='category_products'),
    path('create_product/', create_product, name='create_product'),
]
