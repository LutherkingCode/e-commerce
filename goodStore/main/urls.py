from django.urls import path

from . import views
urlpatterns = [
    
    path('', views.home, name='home'),
      path('login', views.home,name='login'),
       path('cart_view', views.cart_view,name='cart_view'),
        path('products_details', views.product_details,name='product_details'),
        path('product_list', views.product_list,name='product_list'),
                path('checkout', views.checkout,name='checkout'),
    
] 