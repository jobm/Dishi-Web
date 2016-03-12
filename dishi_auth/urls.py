from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static


urlpatterns = [
        url(r'^accounts/', include('allauth.urls')),
        # url(r'^accounts/profile/', TemplateView.as_view(template_name='profile.html'), name="profile")
    ]
