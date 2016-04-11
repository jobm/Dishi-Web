from django.conf.urls import url
from dishi_kitchen import views


# url for a kitchen
urlpatterns = [
    url(r'^$', views.kitchen_home, name="home"),
    url(r'^create/$', views.create_kitchen, name="create_kitchen"),

    url(r'^menu/$', views.kitchen_menu, name="menu"),
    url(r'^recipe/$', views.kitchen_recipe, name="recipe"),

    url(r'^menu/create/$', views.add_kitchen_menu, name="add_menu"),
    url(r'^recipe/create/$', views.add_kitchen_recipe, name="add_recipe"),

    url(r'^menu/like/$', views.like_kitchen_menu, name="like_menu"),
    url(r'^menu/unlike/$', views.unlike_kitchen_menu, name="unlike_menu"),

    url(r'^follow/$', views.follow_kitchen, name="follow"),
    url(r'^unfollow/$', views.un_follow_kitchen, name="un_follow"),
]
