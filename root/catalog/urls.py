from django.conf.urls import url
from django.urls import path, re_path
from . import views
from .views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('details', details),
    path('create', create),
    path('ajax_select', ajax_select),
    re_path(r'^update/(?P<id>[0-9]+)$', update),
    re_path(r'^delete/(?P<id>[0-9]+)$', delete),
    re_path(r'^select/(?P<cid>[0-9]+)$', select)
]

