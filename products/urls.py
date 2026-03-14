from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:product_id>/', views.update_cart, name='update_cart'),
    path('',views.home, name='home'),
    path('checkout/', views.checkout, name='checkout'),
    path('artist/<int:artist_id>/', views.artist_profile, name='artist_profile')
    
]