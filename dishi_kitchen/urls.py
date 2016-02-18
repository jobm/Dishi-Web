from django.conf.urls import url, include
from dishi_kitchen import views


# url for a kitchen
app_name = 'dishi_kitchen'
urlpatterns = [
    url('(?P<username>[\w-]+)/$', views.kitchen_home, name="kitchen"),
    url('menu/add/$', views.kitchen_menu, name="kitchen_menu"),
    url('recipe/add/$', views.kitchen_menu, name="kitchen_recipe"),
    url('menu/create/$', views.add_kitchen_menu, name="add_kitchen_menu"),
    url('recipe/create/$', views.add_kitchen_recipe, name="add_recipe_menu"),
]
