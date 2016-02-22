from django.conf.urls import url, include
from dishi_kitchen import views


# url for a kitchen
urlpatterns = [
    url('^(?P<username>[\w-]+)/$', views.kitchen_home, name="kitchen"),
    url('^(?P<username>[\w-]+)/menu/$', views.kitchen_menu, name="menu"),
    url('^(?P<username>[\w-]+)/recipe/$', views.kitchen_menu, name="recipe"),
    url('^(?P<username>[\w-]+)/menu/create/$', views.add_kitchen_menu, name="add_menu"),
    url('^(?P<username>[\w-]+)/recipe/create/$', views.add_kitchen_recipe, name="add_recipe"),
    url('^(?P<username>[\w-]+)/kitchen/create/$', views.create_kitchen, name="create_kitchen")
]
