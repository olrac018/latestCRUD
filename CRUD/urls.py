from django.conf.urls import url

from CRUD import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^list$', views.std_list, name='std_list'),
    url(r'^create$', views.std_create, name='std_create'),
    url(r'^update/(?P<pk>\d+)$', views.std_update, name='std_update'),
    url(r'^delete/(?P<pk>\d+)$', views.std_delete, name='std_delete'),
        
]
