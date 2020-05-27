from django.urls import path
from . import views
from django.urls import path, include


urlpatterns = [
    path(r'', views.index, name= 'home'),
    path(r'^add/$', views.add, name= 'add'),
    path(r'^delete/$', views.delete, name= 'delete'),
    path(r'^login/$', views.login, name = 'login'),
    path(r'^data/$', views.data, name = 'data'),
    path(r'^delete_autor/$', views.delete_autor, name= 'delete_autor'),
    path(r'domu', views.domu, name= 'domu'), 


]
