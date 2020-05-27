from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.index, name= 'home'),
    path(r'^add/$', views.add, name= 'add'),
    path(r'^login/$', views.login, name = 'login'),
    path(r'^data/$', views.data, name = 'data')

]
