from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.landing_page, name="home"),
    url(r'^complete/profile/$', views.show_user_form, name="complete_profile"),
    url(r'^profile/save/$', views.user_registration, name="save_profile"),
    url(r'^chef/', include('dishi_chef.urls', namespace='dishi_chef')),
]
