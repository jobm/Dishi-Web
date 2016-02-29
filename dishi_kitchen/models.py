from django.db import models
import uuid as h
from dishi_chef.models import Chef
from shared_files.dishi_user import (DishiUser, DishItem,
                                     BUSSINES_TYPE_CHOICES,
                                     KITCHEN_TYPE_CHOICES,)
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# model to create a Kitchen
class Followers(models.Model):
    follower = models.ForeignKey(User, blank=True)
    date_followed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.follower.username


class Following(models.Model):
    following = models.ForeignKey(User, blank=True)
    date_following = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.following.username


class Kitchen(models.Model):
    kitchen_name = models.CharField(max_length=50, blank=False)
    business_type = models.CharField(max_length=50, blank=False)
    kitchen_type = models.CharField(max_length=50, blank=False)
    """"this field creates a relationship to a chef identifying them as an
    owner of a kitchen meaning one chef one kitchen"""
    owner = models.OneToOneField(Chef, primary_key=True)
    followers = models.ManyToManyField(Followers, related_name="kitchen_followers", symmetrical=False)
    following = models.ManyToManyField(Following, related_name="kitchen_following", symmetrical=False)
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


# this is field to create a list of members
# class Member(models.Model):
#     user_name = models.CharField(max_length=50, blank=True)
#     date_created = models.DateTimeField(auto_now=True)
#     date_updated = models.DateTimeField(auto_now_add=True)


# model for a kitchens Team
# class Team(models.Model):
#     name = models.CharField(max_length=50, blank=True)
#     """this is a field to create multiple fields to store members user_names
#     it relates to the "member" model above as a Many To Many relationship"""
#     members = models.ManyToManyField(Member)
#     """"this field creates a relationship to a kitchen identifying it as an
#     onwerof a Team meaning one Kitchen one Team"""
#     kitchen = models.OneToOneField(Kitchen, primary_key=True)
#     date_created = models.DateTimeField(auto_now=True)
#     date_updated = models.DateTimeField(auto_now_add=True)
#
# """ your invitation model should store a unique,
#     random token and ForeignKey to the chef's kitchen
#     you send e-mail with a link with that token,
#     then you look up the tokens in the view"""


# kitchen post model
# class Post(models.Model):
#     pass


# invite model
class Invite(models.Model):
    # owner = models.ForeignKey(User)
    recipient_email = models.EmailField(blank=False)
    hash_token = models.CharField(blank=False, unique=True, max_length=36)

    # method to generate unique token
    def generate_unique_hash(self):
        return str(h.uuid5(hash.NAMESPACE_URL, self.recipient_email))
    # override save method
    # def save(self, *args, **kwargs):
    #     if not self.hash_token:
    #         self.hash_token = self.generate_unique_hash()
    #     super(self, Invite).save(*arg, **kwargs)
