"""
URL configuration for Order project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import Main_page.views as main_views
import Сontact_page.views as contact_views
import Shopping_cart_page.views as shop_cart_views
import Product_page.views as product_views
import Authorization_Registration.views as auth_views
import Authorization_Registration.views as reg_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.main_func, name='main_page'),
    path('contact/', contact_views.contact_func, name='contact_page'),
    path('shop_cart/', shop_cart_views.shop_cart_func, name='shop_cart_page'),
    path('product/', product_views.product_func, name='product_page'),
    path('auth/', auth_views.auth_func, name='auth_page'),
    path('reg/', reg_views.reg_func, name='reg_page'),
]
