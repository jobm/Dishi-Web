from django import forms
from dishi_chef.models import Chef
from django_summernote.widgets import SummernoteWidget


# form to create a chef, currently not working
class ChefForm(forms.ModelForm):
    class Meta:
        model = Chef
        fields = ['username', 'email', 'first_name', 'last_name', 'about_chef']
        widgets = {
            'about_chef': SummernoteWidget(),
        }
