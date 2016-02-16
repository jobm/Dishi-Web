from django.shortcuts import render, redirect
# from dishi_chef.forms import KitchenForm, InviteForm
from dishi_chef.models import Chef
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from shared_files.dishi_user import get_object_or_none
from dishi_chef.forms import ChefForm


LOGIN_URL = "/auth/accounts/login/"


# Create your views here.
@login_required(login_url=LOGIN_URL)
def kitchen_home(request):
    # pre save the user partly
    save_user_as_chef(request)
    # check if the requesting user is an existing chef
    chef = get_object_or_none(Chef, pk=request.user.pk)
    # if not an existing chef render a form to save the rest of his info
    if not chef.first_name:
        chef_form = ChefForm()
        return render(request, 'chef_reg_form.html',
                      context={"chef_form": chef_form})
    # if an existing chef redirect him to his profile page
    return render(request, "chef_home.html", context={"chef": chef})


# save user as chef when they access the chef section
def save_user_as_chef(request):
    if not get_object_or_none(Chef, pk=request.user.pk):
        chef = Chef()
        chef.pk = request.user.pk
        chef.id = request.user.id
        chef.owner = request.user
        chef.user_name = request.user.username
        chef.email = request.user.email
        chef.is_chef = True
        chef.save()
    else:
        pass

