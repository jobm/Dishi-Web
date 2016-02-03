from django import forms
from .models import Chef, Kitchen
from shared_files.dishi_user import BUSSINES_TYPE_CHOICES, KITCHEN_TYPE_CHOICES


# form to create a chef, currently not working
class ChefForm(forms.ModelForm):
    # add chef fields here
    pass


# this form should only have about three fields for now
class KitchenForm(forms.ModelForm):

    class Meta:
        model = Kitchen
        fields = ['kitchen_name', 'bussiness_type', 'kitchen_type']
    bussiness_type = forms.ChoiceField(
        choices=BUSSINES_TYPE_CHOICES, widget=forms.RadioSelect)

    kitchen_type = forms.ChoiceField(
        choices=KITCHEN_TYPE_CHOICES, widget=forms.SelectMultiple)
