from django.db import models
from django.contrib.auth.models import User
from shared_files.dishi_user import DishiUser


# Create your models here.
class Chef(DishiUser):
    is_chef = models.BooleanField(default=False)
    about_chef = models.TextField(verbose_name="about you")
    owner = models.OneToOneField(User, unique=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
