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

    url(r'^menu/(?P<pk>[0-9]+)/edit/$', views.edit_kitchen_menu, name="edit_menu"),
    url(r'^menu/(?P<pk>[0-9]+)/update/$', views.update_kitchen_menu, name="update_menu"),
    url(r'^menu/(?P<pk>[0-9]+)/delete/$', views.delete_kitchen_menu, name="delete_menu"),


    url(r'^recipe/(?P<pk>[0-9]+)/edit/$', views.edit_kitchen_recipe, name="edit_recipe"),
    url(r'^recipe/(?P<pk>[0-9]+)/update/$', views.update_kitchen_recipe, name="update_recipe"),
    url(r'^recipe/(?P<pk>[0-9]+)/delete/$', views.delete_kitchen_recipe, name="delete_recipe"),


    url(r'^menu/like/$', views.like_kitchen_menu, name="like_menu"),
    url(r'^menu/unlike/$', views.unlike_kitchen_menu, name="unlike_menu"),

    url(r'^follow/$', views.follow_kitchen, name="follow"),
    url(r'^unfollow/$', views.un_follow_kitchen, name="un_follow"),

    url(r'^menu/(?P<pk>[0-9]+)/bookmark/', views.bookmark_menu_item, name="bookmark_menu"),
    url(r'^menu/(?P<pk>[0-9]+)/unbookmark/', views.remove_menu_bookmark, name="un_bookmark_menu"),

    url(r'^recipe/(?P<pk>[0-9]+)/bookmark/', views.bookmark_recipe_item, name="bookmark_recipe"),
    url(r'^recipe/(?P<pk>[0-9]+)/unbookmark/', views.remove_recipe_bookmark, name="un_bookmark_reccipe"),
]
