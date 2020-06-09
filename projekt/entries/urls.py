from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.index, name='home'),
    path(r'^add/$', views.add, name='add'),
    path(r'add_data/', views.add_data, name='add_data'),
    path(r'^delete/$', views.delete, name='delete'),
    path(r'^login/$', views.login, name='login'),
    path(r'^data/$', views.data, name='data'),
    path(r'delete_autor/<int:id>', views.delete_autor, name='delete_autor'),
    path(r'edit/<int:id>', views.edit, name='edit'),
    path(r'edit_data/<int:id>',views.edit_data,name='edit_data'),
    path(r'domu', views.domu, name='domu'),



]
