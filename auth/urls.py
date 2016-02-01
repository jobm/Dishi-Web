from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from auth import views


urlpatterns = [
        url(r'^$', views.auth_home),
        url(r'accounts/', include('registration.backends.default.urls')),
    ]
