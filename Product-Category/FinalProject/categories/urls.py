from django.conf.urls import url
from . import views
app_name='categories'


urlpatterns = [
    url(r'^$', views.categories, name="list"), 
    url(r'^create/$', views.catergory_create, name="create"), 
    url(r'^(?P<slug>[\w-]+)/$', views.catergory_detail), 

]
