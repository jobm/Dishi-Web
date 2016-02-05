from django.db import models
from django.contrib.auth.models import User
from shared_files.dishi_user import Dishi_User, Dish_Item
from django.core.validators import MinValueValidator, MaxValueValidator


#Create your models here.
class Chef(Dishi_User):
    """this field creates a relationship to a user of dishi identifying them as
    a type of a user"""
    #owner = models.OneToOneField(User, unique=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

# model to create a Kitchen
class Kitchen(models.Model):

    kitchen_types=[('a', 'Bakery'),
                    ('b', 'African Cuisine'),
                    ('c', 'Intercontinental Cuisine'), ]

    Kitchen_choices=[('a', 'Start a Food Business'),
                        ('b', 'Scale an existing food business'),
                        ('c', 'Sell food in my spare time'),
                        ('d','Offer cooking classes'), ]

    full_name=models.CharField(
        max_length=120, blank=False, null=True)

    email=models.EmailField(
        blank=False, null=True)

    password=models.CharField(
        max_length=20, blank=False, null=True)

    confirm_password=models.CharField(
        max_length=20, blank=False, null=True)

    kitchen_name = models.OneToOneField(
        Chef, primary_key=True)

    #multiple choice fields
    """ this is a field to create multiple fields to store members user_names
    it relates to the "kitchen_types" model above as a Many To Many
    relationship"""

    kitchen_type = models.CharField(
        max_length=1, blank=False, choices=kitchen_types)

    bussiness_type =models.CharField(
        max_length=1, blank=False, choices=Kitchen_choices)

    """"this field creates a relationship to a chef identifying them as an onwer
    of a kitchen meaning one chef one kitchen"""
    date_created = models.DateTimeField(auto_now=True)

    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


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
