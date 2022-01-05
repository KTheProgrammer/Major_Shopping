from django.urls import path 
from . import views
from .models import *
from django.contrib import admin

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('register/', views.register),
    path('login/', views.login),
    path('logout', views.logout),

    path('<int:product_id>/product', views.product),
    path('checkout/', views.checkout),
    path('update_order/', views.updateOrder),
    path('user/', views.user),
    path('cart/', views.cart),
    path('create', views.create)
]
