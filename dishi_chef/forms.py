from django import forms
from .models import Chef, Kitchen, Invite
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

    bussiness_type = forms.MultipleChoiceField(
        label="What kind of kitchen do you need?",
        choices=BUSSINES_TYPE_CHOICES, widget=forms.RadioSelect(
            attrs={'class': 'radio_field'}
        ))

    kitchen_type = forms.MultipleChoiceField(
        choices=KITCHEN_TYPE_CHOICES, widget=forms.Select)


# this a form to invite a user to a kitchen
class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = ['recepient_email']
