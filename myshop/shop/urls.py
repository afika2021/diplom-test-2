from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^delivery/$', views.product_delivery ,name='product_delivery'),
	url(r'^inform/$', views.product_inform ,name='product_inform'),
	url(r'^shop-i/$', views.product_shop_i ,name='product_shop_i'),
	url(r'^$', views.product_main, name='product_main'),
	url(r'^new/$', views.product_new, name='product_new'),
	url(r'^new/(?P<category_slug>[-\w]+)/$', views.product_new, name='product_catalog_new'),
    url(r'^catalog/$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',views.product_list,name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'),

]