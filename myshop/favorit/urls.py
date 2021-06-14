from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.favorit_detail, name='favorit_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.favorit_add, name='favorit_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.favorit_remove, name='favorit_remove'),
]