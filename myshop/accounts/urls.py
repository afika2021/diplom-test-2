from django.conf.urls import url
from . import views 
from .views import register
 
urlpatterns = [
    url(r'^signup/', views.register, name='signup'),
]