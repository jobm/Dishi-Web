from django.contrib import admin
# Register your models here.
from .forms import KitchenForm
from .models import Kitchen

#Class that gives the admin more controll
class KitchenAdmin(admin.ModelAdmin):
	list_display = ["full_name","email"]
	# below is how we say use the model form now! 
	form = KitchenForm
	# class Meta:
	# 	model=Subscribe	
			
admin.site.register(Kitchen,KitchenAdmin)	