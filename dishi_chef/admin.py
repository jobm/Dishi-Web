from django.contrib import admin
# Register your models here.
from .forms import KitchenForm,ChefForm
from .models import Kitchen ,Chef

class ChefAdmin(admin.ModelAdmin):
	list_display = ['first_name','user_name','profile_picture','email_address']
	# below is how we say use the model form now! 
	form = ChefForm
	# class Meta:
	# 	model=Subscribe

#Class that gives the admin more controll
class KitchenAdmin(admin.ModelAdmin):
	list_display = ["full_name","email",'password','confirm_password','kitchen_type','bussiness_type']
	# below is how we say use the model form now! 
	form = KitchenForm
	# class Meta:
	# 	model=Subscribe

	
admin.site.register(Chef,ChefAdmin)				
admin.site.register(Kitchen,KitchenAdmin)
