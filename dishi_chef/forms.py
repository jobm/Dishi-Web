from django import forms
from .models import Chef,business_types,kitchen_types,Kitchen



class KitchenForm(forms.ModelForm):
	Kitchen_choices=[('a','Start a Food Business'),('b','Scale an existing food business'),('c','Sell food in my spare time'),('d','Offer cooking classes'),]
	
	bussiness_type = forms.TypedChoiceField(choices=Kitchen_choices, widget=forms.RadioSelect)

	kitchen_types=[('a','Bakery'),('b','African Cuisine'),('c','Intercontinental Cuisine'),]

	kitchen_type = forms.TypedChoiceField(choices=kitchen_types, widget=forms.RadioSelect)

	class Meta:
		model=Kitchen
		fields=['full_name','email','password','confirm_password','kitchen_type']

	#The below method cleans data and allows for only .com extension emails to be used

	def clean_email(self):
		email=self.cleaned_data.get('email')
		if not ".com" in email:
			raise forms.ValidationError("Please use your moringa email to register")
		return email

	def clean(self):
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		if password and password != confirm_password:
			raise forms.ValidationError("Passwords don't match")
		return self.cleaned_data