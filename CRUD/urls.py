from django.conf.urls import url
from CRUD import views
from CRUD.forms import LoginForm


urlpatterns = [
    url(r'^$', views.home, name='home'), 
    url(r'^index$', views.index, name='index'),
    url(r'^list$', views.std_list, name='std_list'),
    url(r'^create$', views.std_create, name='std_create'),
    url(r'^update/(?P<pk>\d+)$', views.std_update, name='std_update'),
    url(r'^delete/(?P<pk>\d+)$', views.std_delete, name='std_delete'),
        
]

