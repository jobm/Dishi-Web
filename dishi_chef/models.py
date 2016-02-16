from django.db import models
from shared_files.dishi_user import Dishi_User
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.
class Chef(Dishi_User):
    """this field creates a relationship to a user of dishi identifying them as
    a type of a user"""
    is_chef = models.BooleanField(default=False)
    owner = models.OneToOneField(User, unique=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
