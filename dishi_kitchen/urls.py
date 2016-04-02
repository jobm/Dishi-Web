from django.conf.urls import url
from dishi_kitchen import views


# url for a kitchen
urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', views.kitchen_home, name="home"),
    url(r'^(?P<username>[\w-]+)/menu/$', views.kitchen_menu, name="menu"),
    url(r'^(?P<username>[\w-]+)/recipe/$', views.kitchen_recipe, name="recipe"),

    url(r'^(?P<username>[\w-]+)/menu/create/$', views.add_kitchen_menu, name="add_menu"),
    url(r'^(?P<username>[\w-]+)/menu/like/$', views.like_kitchen_menu, name="like_menu"),
    url(r'^(?P<username>[\w-]+)/menu/unlike/$', views.unlike_kitchen_menu, name="unlike_menu"),


    url(r'^(?P<username>[\w-]+)/recipe/create/$', views.add_kitchen_recipe, name="add_recipe"),
    url(r'^(?P<username>[\w-]+)/kitchen/create/$', views.create_kitchen, name="create_kitchen"),
    url(r'^(?P<username>[\w-]+)/kitchen/follow/$', views.follow_kitchen, name="follow"),
    url(r'^(?P<username>[\w-]+)/kitchen/unfollow/$', views.unfollow_kitchen, name="unfollow"),
]
