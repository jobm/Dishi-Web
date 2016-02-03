from django.conf.urls import url
from dishi_chef import views


# url for a kitchen
urlpatterns = [
    url(r'chef/kitchen/$', views.kitchen_form_view, name='k_form'),
]
