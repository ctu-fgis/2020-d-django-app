from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('entries.urls')),
    url(r'^data/$',include('entries.urls')),
    url(r'^login/$', include('entries.urls')),
    path('accounts/', include('django.contrib.auth.urls')),


]
