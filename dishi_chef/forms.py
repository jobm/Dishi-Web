from django import forms
from dishi_chef.models import Chef
from shared_files.dishi_user import BUSSINES_TYPE_CHOICES, KITCHEN_TYPE_CHOICES


# form to create a chef, currently not working
class ChefForm(forms.ModelForm):
    class Meta:
        model = Chef
        fields = ['user_name', 'first_name', 'last_name', 'tags']
