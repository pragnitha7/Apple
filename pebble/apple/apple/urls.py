"""
URL configuration for apple project.

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
import customer.views as cust_views
import orders.views as order_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',cust_views.register,name='register'),
    path('',cust_views.home,name='home'),
    path('cart/',cust_views.cart,name='cart'),
    path('deleteitem/<int:item_id>',cust_views.deleteitem,name='deleteitem'),
    path('ordernow/<int:item_id>',cust_views.ordernow,name='ordernow'),
    path('orders/',cust_views.pastorders,name='order'),
    path('contact_us/',cust_views.contact,name='contact'),
    path('profile/<int:id>',cust_views.profile,name='profile'),
    path('update_profile/<int:id>',cust_views.updateprofile,name='updateprofile'),
    path('add_to_cart/<int:id>/', cust_views.add_to_cart, name='add_to_cart'),
    path('restaurant_detail/<int:restaurant_id>',cust_views.restaurant_detail,name='restaurant_detail'),
    path('category_detail/<int:category_id>',cust_views.category_detail,name='category_detail'),
    path('login/',auth_views.LoginView.as_view(template_name='customer/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='customer/logout.html'),name='logout'),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
