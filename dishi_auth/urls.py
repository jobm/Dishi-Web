from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static


urlpatterns = [
        # url(r'^accounts/', include('registration.backends.default.urls')),
        url(r'^accounts/', include('allauth.urls')),
    ]
