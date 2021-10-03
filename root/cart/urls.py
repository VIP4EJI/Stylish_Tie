from django.urls import path
from django.conf.urls import url
from . import views
from .views import *

urlpatterns = [
    path('cart_detail', cart_detail),
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('index', index),
    path('confirm', confirm),
    path('ajax_basket', ajax_basket),
    path('ajax_basket_display', ajax_basket_display),

    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),

]
