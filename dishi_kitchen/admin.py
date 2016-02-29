from django.contrib import admin
from .models import Kitchen, Recipe, Menu, Followers

# Register your models here.
admin.site.register(Kitchen)
admin.site.register(Recipe)
admin.site.register(Menu)
admin.site.register(Followers)
