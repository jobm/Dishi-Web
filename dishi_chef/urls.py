from django.conf.urls import url, include
from dishi_chef import views


# url for a kitchen
urlpatterns = [
    url(r'chef/$', views.kitchen_home, name='home'),
    url(r'chef/save_reg_form/$', views.save_chef_reg_form, name='save_reg_form'),
    url(r'chef/kitchen/', include('dishi_kitchen.urls',
        namespace='chef_kitchen')),

    # url(r'chef/kitchen/$', views.kitchen_form_view, name='k_form'),
    # url(r'chef/invite/$', views.invite_team, name='i_form'),
]
