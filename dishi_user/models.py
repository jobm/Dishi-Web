from django.db import models
from shared_files.dishi_user import DishiUser
from django.contrib.auth.models import User
from dishi_kitchen.models import Recipe, Menu


# Create your models here.
class NormalUser(DishiUser):
    owner = models.OneToOneField(User, unique=True, primary_key=True)


class MenuBookmark(models.Model):
    owner = models.OneToOneField(User)
    menu_item = models.ForeignKey(Menu)


class RecipeBookmark(models.Model):
    owner = models.OneToOneField(User)
    menu_item = models.ForeignKey(Recipe)

