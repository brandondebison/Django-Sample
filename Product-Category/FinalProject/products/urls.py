from django.conf.urls import url
from . import views
app_name='products'

urlpatterns = [
    url(r'^$', views.product_list, name="list"), 
    url(r'^create/$', views.product_create, name="create"), 
    url(r'^(?P<slug>[\w-]+)/$', views.product_detail, name="detail"), 
]
