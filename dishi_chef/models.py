from django.db import models
from django.contrib.auth.models import User
from shared_files.dishi_user import Dishi_User, Dish_Item, Dish_Created_At
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Chef(Dishi_User):
    """this field creates a relationship to a user of dishi identifying them as
    a type of a user"""
    owner = models.OneToOneField(User, unique=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)


# a list of business types it's just a field in the Kitchen model
class business_types(models.Model):
    bussiness_type = models.CharField(max_length=50, blank=False)


# a list of kitchen types it's just a field in the Kitchen model
class kitchen_types(models.Model):
    kitchen_type = models.CharField(max_length=50, blank=False)


# model to create a Kitchen
class Kitchen(models.Model):
    kitchen_name = models.CharField(max_length=50, blank=True)
    """ this is a field to create multiple fields to store members user_names
    it relates to the "kitchen_types" model above as a Many To Many
    relationship"""
    bussiness_types = models.ManyToManyField(business_types)
    kitchen_type = models.ManyToManyField(kitchen_types)
    """"this field creates a relationship to a chef identifying them as an onwer
    of a kitchen meaning one chef one kitchen"""
    owner = models.OneToOneField(Chef, primary_key=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)


# model to create Kitchens menu
class Menu(Dish_Item):
    cost = models.FloatField(blank=False)
    """this field creates a relationship meaning that a kitchen can have many
    menus"""
    owner = models.ForeignKey(Kitchen)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)


# model to create a recipe
class Recipe(Dish_Item):
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


# this is field to createa a list of members
class member(models.Model):
    user_name = models.CharField(max_length=50, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)


# model for a kitchens Team
class Team(models.Model):
    name = models.CharField(max_length=50, blank=True)
    """this is a field to create multiple fields to store members user_names
    it relates to the "member" model above as a Many To Many relationship"""
    members = models.ManyToManyField(member)
    """"this field creates a relationship to a kitchen identifying it as an
    onwerof a Team meaning one Kitchen one Team"""
    kitchen = models.OneToOneField(Kitchen, primary_key=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
