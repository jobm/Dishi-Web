from django import forms
from .models import Chef, business_types, kitchen_types, Kitchen

"""
look into crispy-forms-foundation and model the forms around that, it also
comes with validation called 'abide' look at that as well, it may prove abit
challenging but incase of problems, tell me.
"""


# create a chef form here"""
class ChefForm(forms.ModelForm):
    # add chef fields here
    pass


# this form should only have about three fields for now
class KitchenForm(forms.ModelForm):

    class Meta:
        model = Kitchen
        fields = ['kitchen_name', 'bussiness_type', 'kitchen_type']
    bussiness_type = forms.ChoiceField(
        choices=Kitchen_choices, widget=forms.RadioSelect)

    kitchen_type = forms.ChoiceField(
        choices=kitchen_types, widget=forms.SelectMultiple)

    # The below method cleans data and allows for only .com extension emails
    # to be used
    # we wont need to do form validation for now but we will revisit it later
    """
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if ".com" not in email:
            raise forms.ValidationError(
                "Please use your moringa email to register")
        return email

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return self.cleaned_data
    """
