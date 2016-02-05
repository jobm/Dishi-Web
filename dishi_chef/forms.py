from django import forms
from .models import Chef, Kitchen
from crispy_forms_foundation.forms import FoundationModelForm
from crispy_forms.helper import FormHelper


"""
look into crispy-forms-foundation and model the forms around that, it also
comes with validation called 'abide' look at that as well, it may prove abit
challenging but incase of problems, tell me.
"""

class ChefForm(FoundationModelForm):

    class Meta:
        model = Chef
        fields = ['user_name', 'first_name', 'last_name',
                    'profile_picture', 'email_address']

    def __init__(self, *args, **kwargs):
        super(FoundationModelForm, self).__init__(*args, **kwargs)
        self.init_helper()


class KitchenForm(forms.ModelForm):
    Kitchen_choices=[('a', 'Start a Food Business'),
                        ('b', 'Scale an existing food business'),
                        ('c', 'Sell food in my spare time'),
                        ('d', 'Offer cooking classes'), ]

    bussiness_type = forms.TypedChoiceField(
        choices=Kitchen_choices, widget=forms.RadioSelect)
    kitchen_types=[('a', 'Bakery'),
	                ('b', 'African Cuisine'),
	                ('c', 'Intercontinental Cuisine'), ]
    kitchen_type = forms.TypedChoiceField(
        choices=kitchen_types, widget=forms.SelectMultiple)
    
    class Meta:
        model=Kitchen
        fields = ['kitchen_name', 'bussiness_type', 'kitchen_type']

	#The below method cleans data and allows for only .com extension emails to be used

    """def clean_email(self):
		email=self.cleaned_data.get('email')
		if not ".com" in email:
			raise forms.ValidationError("Please use your .com email to register")
		return email

	def clean(self):
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		if password and password != confirm_password:
			raise forms.ValidationError("Passwords don't match")
		return self.cleaned_data"""
