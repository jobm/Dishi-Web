from django import forms
from .models import Kitchen, Invite, Menu
from shared_files.dishi_user import BUSSINES_TYPE_CHOICES, KITCHEN_TYPE_CHOICES


# this form should only have about three fields for now
class KitchenForm(forms.ModelForm):

    class Meta:
        model = Kitchen
        fields = ['kitchen_name', 'bussiness_type', 'kitchen_type']

    bussiness_type = forms.MultipleChoiceField(
        label="What kind of kitchen do you need?",
        choices=BUSSINES_TYPE_CHOICES, widget=forms.RadioSelect(
            attrs={'class': 'radio_field'}
        ))

    kitchen_type = forms.MultipleChoiceField(
        choices=KITCHEN_TYPE_CHOICES, widget=forms.Select)


# menu form
class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["title", "item_picture", "description", "cost"]


# Recipe form
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        field = ["title", "item_picture", "description", "cost"]


# this a form to invite a user to a kitchen
class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = ['recepient_email']
