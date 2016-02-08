from django.conf.urls import include, url
from django.contrib import admin
from django .conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    url(r'^$', 'dishi_chef.views.Chef', name='chef'),
    url(r'^index/', 'dishi_chef.views.kitchen', name='kitchen'),   
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
