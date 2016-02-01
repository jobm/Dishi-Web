from django.conf.urls import include, url
from django.contrib import admin
# from django.auth import urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'Dishi_Web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^auth/', include('auth.urls', namespace='auth')),
    url(r'^admin/', include(admin.site.urls)),
]
