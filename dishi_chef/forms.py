from django import forms
from dishi_chef.models import Chef
from django_summernote.widgets import SummernoteWidget


# form to create a chef, currently not working
class ChefForm(forms.ModelForm):
    class Meta:
        model = Chef
        exclude = ['date_created', 'date_updated', "owner", "is_chef"]
        # fields = ['username', 'email', 'first_name', 'last_name', 'about_chef']
        widgets = {
            'about_chef': SummernoteWidget(),
        }
