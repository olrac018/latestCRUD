from django.conf.urls import include, url

from login import views
 
urlpatterns = [
    url(r'^$', views.login, name ='login'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^logout/$', views.logout, name ='logout'),
    url(r'^register/$', views.register, name='register' ),
    url(r'^register/success/$', views.register_success, name ='register_success'),
]