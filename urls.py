from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("products",views.products, name='products'),
    path("contact",views.contact, name='contact'),
    path("category",views.category,name='category'),
    path("cart",views.Cart,name='cart'),
    # path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    # path('remove_from_cart/<int:item_id>', views.remove_from_cart, name='remove_from_cart'),
    # path('view_cart', views.view_cart, name='view_cart'),

]
