from django import forms
from .models import Chef
from shared_files.dishi_user import BUSSINES_TYPE_CHOICES, KITCHEN_TYPE_CHOICES


# form to create a chef, currently not working
class ChefForm(forms.ModelForm):
    # add chef fields here
    pass
