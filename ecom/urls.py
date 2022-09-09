"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from products.views import product_detail_all_view, product_detail_view, product_search_view
from pages.views import pages_home_view, pages_login_view, pages_register_view

urlpatterns = [
    path('home/', pages_home_view),
    path('admin/', admin.site.urls),
    path('search/', product_search_view),
    path('products/', product_detail_view),
    path('register/', pages_register_view),
    path('login/', pages_login_view),
    path('products_all/', product_detail_all_view),
]
