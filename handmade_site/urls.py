"""
URL configuration for handmade_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from products import views

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('shop/', views.shop, name='shop'),  # Shop page
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # Product detail page

    # Auth URLs (login/logout/password)
    path('accounts/', include('django.contrib.auth.urls')),

    # Signup page under /accounts/signup/
    path('accounts/', include('products.urls')),
    path('', include('products.urls')),  # Include product app URLs
]

# Serve media files (optional)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

