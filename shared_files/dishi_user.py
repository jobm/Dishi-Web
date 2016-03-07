from django.db import models


# shared user models
class DishiUser(models.Model):
    username = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    profile_picture = models.ImageField(blank=True)

    class Meta:
        abstract = True


class DishItem(models.Model):
    title = models.CharField(max_length=50, blank=False)
    item_picture = models.ImageField(blank=True)
    description = models.TextField()

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
