from django.db import models
import uuid as h
from dishi_chef.models import Chef
from shared_files.dishi_user import DishItem
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# model to create a Kitchen
class Follower(models.Model):
    follower = models.ForeignKey(User, blank=True)
    date_followed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.follower.username


class Kitchen(models.Model):
    kitchen_name = models.CharField(max_length=50, blank=False)
    business_type = models.CharField(max_length=50, blank=False)
    kitchen_type = models.CharField(max_length=50, blank=False)
    about_kitchen = models.TextField(verbose_name="kitchen description")
    cover_image = models.ImageField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True, default="+xxx-xxx-xxx-xxx")
    logo = models.ImageField(blank=True)
    secondary_email = models.EmailField(blank=True, default="example@example.com")
    """"this field creates a relationship to a chef identifying them as an
    owner of a kitchen meaning one chef one kitchen"""
    owner = models.OneToOneField(Chef, primary_key=True)
    followers = models.ManyToManyField(Follower,
                                       related_name="kitchen_follower",
                                       symmetrical=False)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.kitchen_name


# model to hold the comments of a conversation
class Comment(models.Model):
    comment = models.TextField()
    commenter = models.ForeignKey(User, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)


# model to hold the like of a conversation
class Like(models.Model):
    like = models.IntegerField()
    liker = models.ForeignKey(User, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)


# model to create a kitchen's conversation
class Conversation(models.Model):
    title = models.CharField(max_length=50, blank=False)
    post = models.TextField()
    publisher = models.CharField(max_length=50, blank=False)
    comments = models.ManyToManyField(Comment,
                                      related_name="kitchen_comment",
                                      symmetrical=False)
    likes = models.ManyToManyField(Like,
                                  related_name="kitchen_like",
                                  symmetrical=False)
    owner = models.ForeignKey(Kitchen)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)


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
    ingredients = models.TextField(blank=True)
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
