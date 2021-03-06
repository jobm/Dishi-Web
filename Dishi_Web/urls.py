from django.conf.urls import include, url
from django.contrib import admin
from Dishi_Web import views
urlpatterns = [
    url(r'^$', views.landing_page, name='landing'),
    url(r'^auth/', include('dishi_auth.urls')),
    url(r'^chef/', include('dishi_chef.urls', namespace='dishi_chef')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')),
]
