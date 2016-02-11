from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^dishi/', include('dishi_chef.urls', namespace='dishi_chef')),
    url(r'^auth/', include('dishi_auth.urls', namespace='dishi_auth')),
    url(r'^admin/', include(admin.site.urls)),
]
