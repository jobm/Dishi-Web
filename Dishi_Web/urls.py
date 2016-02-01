from django.conf.urls import include, url
from django.contrib import admin
# from django.auth import urls

urlpatterns = [
    url(r'^auth/', include('dishi_auth.urls', namespace='dishi_auth')),
    url(r'^admin/', include(admin.site.urls)),
]
