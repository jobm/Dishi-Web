from django import forms
from .models import Kitchen, Invite, Menu, Recipe
from shared_files.dishi_user import BUSINESS_TYPE_CHOICES, KITCHEN_TYPE_CHOICES
from django_summernote.widgets import SummernoteWidget


# this form should only have about three fields for now
class KitchenForm(forms.ModelForm):

    class Meta:
        model = Kitchen
        fields = ['kitchen_name', 'business_type', 'kitchen_type',
                  'about_kitchen', 'phone_number', 'secondary_email']

    business_type = forms.ChoiceField(
        label="What kind of kitchen do you need?",
        choices=BUSINESS_TYPE_CHOICES, widget=forms.RadioSelect(
        ))

    kitchen_type = forms.ChoiceField(
        label="What type of kitchen do you need?",
        choices=KITCHEN_TYPE_CHOICES, widget=forms.Select)

    about_kitchen = forms.CharField(
        label="description of your kitchen",
        widget=SummernoteWidget)


# menu form
class MenuAddForm(forms.ModelForm):
    class Meta:
        model = Menu
        exclude = ["owner", "comments", "likes"]
        # fields = ["title", "item_picture", "description", "cost"]


# menu edit form
class MenuEditForm(forms.ModelForm):
    class Meta:
        model = Menu
        exclude = ["owner", "comments", "likes"]


# Recipe form
class RecipeAddForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "item_picture", "description", "ingredients"]
    description = forms.CharField(label="how to prepare", widget=SummernoteWidget)


# Recipe Edit Form
class RecipeEditForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "item_picture", "description", "ingredients"]
    description = forms.CharField(label="how to prepare", widget=SummernoteWidget)


# this a form to invite a user to a kitchen
class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = ['recipient_email']
