from django.db import models
from django.contrib.auth.models import User


# shared user models
class DishiUser(models.Model):
    # username = models.CharField(max_length=50, blank=True, default="your username")
    # first_name = models.CharField(max_length=50, blank=False, default="your first name")
    # last_name = models.CharField(max_length=50, blank=False, default="your last name")
    # email = models.EmailField(max_length=50, blank=False, default="example@example.com")
    profile_picture = models.ImageField(blank=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class DishItem(models.Model):
    title = models.CharField(max_length=50, blank=False)
    item_picture = models.ImageField(blank=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Like(models.Model):
    liker = models.ForeignKey(User, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Comment(models.Model):
    comment = models.TextField()
    commenter = models.ForeignKey(User, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


# this fields are use for the multi-select/choice fields of the chef model
BUSINESS_TYPE_CHOICES = [
    ('type_1', 'Start a Food Business'),
    ('type_2', 'Scale an existing food business'),
    ('type_3', 'Sell food in my spare time'),
    ('type_4', 'Offer cooking classes'),
]
KITCHEN_TYPE_CHOICES = [
    ('type_1', 'bakery'),
    ('type_2', 'cuisine'),
    ('type_3', 'African'),
    ('type_4', 'Other'),
]


# reused methods
# this methods checks whether a model exists if it does its returned else it returns None
def get_object_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except models.ObjectDoesNotExist:
        return None


def filter_object_or_none(model, *args, **kwargs):
    try:
        return model.objects.filter(*args, **kwargs)
    except models.ObjectDoesNotExist:
        return None
