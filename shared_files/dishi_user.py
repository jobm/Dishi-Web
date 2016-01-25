from django.db import models


# shared user models
class Dishi_User(models.Model):
    user_name = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    profile_picture = models.ImageField(blank=True)
    email_address = models.EmailField(max_length=50, blank=False)

    class Meta:
        abstract = True


class Dish_Item(models.Model):
    title = models.CharField(max_length=50, blank=False)
    item_picture = models.ImageField(blank=True)
    description = models.TextField()

    class Meta:
        abstract = True
