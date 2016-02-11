from django.contrib import admin
from .models import Chef
from dishi_kitchen.models import Kitchen
# Register your models here.
admin.site.register(Chef)
admin.site.register(Kitchen)
