from django.contrib.auth.models import User
from django import forms


# create form to add a user here
class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ['username', 'email', 'first_name', 'last_name']
