from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('dishi_user.urls', namespace="dishi_user")),
    url(r'^auth/', include('dishi_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^activity/', include('actstream.urls')),
    url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
]
