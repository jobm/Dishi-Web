from django.db import models
import uuid as h
from dishi_chef.models import Chef
from shared_files.dishi_user import DishItem
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# model to create a Kitchen
class Followers(models.Model):
    follower = models.ForeignKey(User, blank=True)
    date_followed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.follower.username


class Kitchen(models.Model):
    kitchen_name = models.CharField(max_length=50, blank=False)
    business_type = models.CharField(max_length=50, blank=False)
    kitchen_type = models.CharField(max_length=50, blank=False)
    about_kitchen = models.TextField(verbose_name="kitchen description")
    """"this field creates a relationship to a chef identifying them as an
    owner of a kitchen meaning one chef one kitchen"""
    owner = models.OneToOneField(Chef, primary_key=True)
    followers = models.ManyToManyField(Followers, related_name="kitchen_followers", symmetrical=False)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.kitchen_name


# model to create Kitchens menu
class Menu(DishItem):
    cost = models.FloatField(blank=False)
    """this field creates a relationship meaning that a kitchen can have many
    menus"""
    owner = models.ForeignKey(Kitchen)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)


# model to create a recipe
class Recipe(DishItem):
    # comma separated field of instructions
    ingredients = models.CharField(blank=True, max_length=1000)
    likes = models.IntegerField(blank=True,
                                validators=[
                                    MinValueValidator(1),
                                    MaxValueValidator(50)
                                ])
    """this field creates a relationship meaning that a kithen can create many
    recipes"""
    owner = models.ForeignKey(Kitchen)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)


# invite model
class Invite(models.Model):
    # owner = models.ForeignKey(User)
    recipient_email = models.EmailField(blank=False)
    hash_token = models.CharField(blank=False, unique=True, max_length=36)

    # method to generate unique token
    def generate_unique_hash(self):
        return str(h.uuid5(h.NAMESPACE_URL, self.recipient_email))
    # override save method
    # def save(self, *args, **kwargs):
    #     if not self.hash_token:
    #         self.hash_token = self.generate_unique_hash()
    #     super(self, Invite).save(*arg, **kwargs)
