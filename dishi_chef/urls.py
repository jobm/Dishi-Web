from django.conf.urls import url, include
from dishi_chef import views

# url for a kitchen
urlpatterns = [
    url(r'^$', views.chef_home, name='home'),
    url(r'^(?P<username>[\w-]+)/save_reg_form/$', views.save_chef_reg_form, name='save_reg_form'),
    url(r'^(?P<username>[\w-]+)/kitchen/', include('dishi_kitchen.urls', namespace='kitchen')),
]
