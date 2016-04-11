from django.db import models
from django.contrib.auth.models import User
from shared_files.dishi_user import DishiUser


# Create your models here.
class Chef(DishiUser):
    is_chef = models.BooleanField(default=False)
    about_chef = models.TextField(verbose_name="about you")
    owner = models.OneToOneField(User, unique=True, primary_key=True)

    def __str__(self):
        return self.username
