from django.db import models
import uuid as h
from dishi_chef.models import Chef
from shared_files.dishi_user import DishItem, Like, Comment
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# model to create a Kitchen
class Follower(models.Model):
    follower = models.OneToOneField(User, unique=True, blank=True)

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
    owner = models.OneToOneField(Chef, unique=True, primary_key=True)
    followers = models.ManyToManyField(Follower)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.kitchen_name


# model to hold the comments of a conversation
class ConversationComment(Comment):
    def __str__(self):
        return self.commenter.username


# model to hold the like of a conversation
class ConversationLike(Like):
    def __str__(self):
        return self.liker.username


# model to create a kitchen's conversation
class Conversation(models.Model):
    post = models.TextField()
    comments = models.ManyToManyField(ConversationComment,
                                      related_name="kitchen_comment",
                                      symmetrical=False)
    likes = models.ManyToManyField(ConversationLike,
                                   related_name="conversation_like",
                                   symmetrical=False)
    owner = models.ForeignKey(Kitchen)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)


# models to store Menu likes and comments
# Menu likes model
class MenuLike(Like):
    def __str__(self):
        return self.liker.username


# Menu comments model
class MenuComment(Comment):
    def __str__(self):
        return self.commenter.username


# model to create Kitchens menu
class Menu(DishItem):
    cost = models.FloatField(blank=False)
    plates = models.IntegerField(default=1, blank=True,
                                 validators=[
                                    MinValueValidator(1),
                                    MaxValueValidator(50)
                                 ])
    remaining_plates = models.IntegerField(default=1, blank=True,
                                           validators=[
                                               MinValueValidator(1),
                                               MaxValueValidator(50)
                                           ])
    comments = models.ManyToManyField(MenuComment,
                                      blank=True,
                                      related_name="menu_comment",
                                      symmetrical=False)
    likes = models.ManyToManyField(MenuLike,
                                   blank=True,
                                   related_name="menu_like",
                                   symmetrical=False)
    """this field creates a relationship meaning that a kitchen can have many
    menus"""
    owner = models.ForeignKey(Kitchen)


# models to store Recipe likes and comments
# Menu likes model
class RecipeLike(Like):
    pass


# Menu comments model
class RecipeComment(Comment):
    pass


# model to create a recipe
class Recipe(DishItem):
    # comma separated field of instructions
    ingredients = models.TextField(blank=True)
    comments = models.ManyToManyField(RecipeComment,
                                      related_name="recipe_comment",
                                      symmetrical=False)
    likes = models.ManyToManyField(RecipeLike,
                                   related_name="recipe_like",
                                   symmetrical=False)
    """this field creates a relationship meaning that a kitchen can create many
    recipes"""
    owner = models.ForeignKey(Kitchen)


# invite model
class Invite(models.Model):
    # owner = models.ForeignKey(User)
    recipient_email = models.EmailField(blank=False)
    hash_token = models.CharField(blank=False, unique=True, max_length=36)

    # method to generate unique token
    def generate_unique_hash(self):
        return str(h.uuid5(h.NAMESPACE_URL, self.recipient_email))
