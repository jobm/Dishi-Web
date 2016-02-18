from django.conf.urls import url, include
from dishi_chef import views


# url for a kitchen
app_name = 'dishi_chef'
urlpatterns = [

    url(r'^(?P<username>[\w-]+)/$', views.chef_home, name='home'),
    url(r'save_reg_form/$', views.save_chef_reg_form, name='save_reg_form'),
]
