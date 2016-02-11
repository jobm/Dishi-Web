from django.conf.urls import url, include
from dishi_kitchen import views


# url for a kitchen
urlpatterns = [
    url('^$', views.kitchen_home, name="kitchen"),
]
