from django.shortcuts import render, redirect
from dishi_chef.models import Chef
from dishi_kitchen.forms import RecipeForm, MenuForm, InviteForm
from shared_files.dishi_user import get_object_or_none
from dishi_kitchen.models import Menu, Recipe, Invite


# url:  /dishi/chef/kitchen/
# Create your views here.
def kitchen_home(request, username):
    chef = get_object_or_none(Chef, username=username)
    return render(request, "kitchen_layout.html", {"chef": chef})


# view to render a form to add a menu item
def kitchen_menu(request, username):
    # menu_item = get_object_or_none(Menu, owner=request.user)
    print(username)
    menu_form = MenuForm()
    context = {"menu_form": menu_form, "username": username}
    return render(request, "menu_add_form.html", context=context)


# view to add the menu item
def add_kitchen_menu(request, username):
    menu_form = MenuForm(request.POST)
    if request.Method == 'POST':
        if menu_form.is_valid():
            menu = menu_form.save(commit=False)
            menu.owner = request.user
            menu.save()
            menu_form.save_m2m()
            return redirect("/kitchen/{}/".format(username))
    return render(request, "menu_add_form.html", context={"menu_form": menu_form})


# view to render a form to add a recipe item
def kitchen_recipe(request, username):
    recipe_form = Recipe()
    context = {"recipe_form": recipe_form, "username": username}
    return render(request, "recipe_add_form.html", context=context)


# view to add recipe item
def add_kitchen_recipe(request, username):
    recipe_form = RecipeForm(request.POST)
    if request.Method == 'POST':
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.owner = request.user
            recipe.save()
            recipe.save_m2m()
            return redirect("/kitchen/{}/".format(username))
    return render(request, "menu_add_form.html", context={"menu_form": recipe_form})


# view to load the blog app
def kitchen_blog(request):
    pass


# create a kitchen form view
"""
def kitchen_form_view(request):
    kitchen_form = KitchenForm(request.POST or None)
    context = {"kitchen_form": kitchen_form}
    return render(request, "kitchen_reg_form.html", context=context)
"""


# view to send an invite
"""
def invite_team(request):
    invite_form = InviteForm(request.POST or None)
    context = {}
    invite = Invite()
    if request.method == 'POST':
        if invite_form.is_valid():
            email = invite_form.cleaned_data.get('recepient_email')
            invite.recepient_email = email
            invite.hash_token = invite.generate_unique_hash()
            # invite.owner = request.user
            # print(email, invite.hash_token, generate_url(invite.hash_token))
            send_mail("Invite to team", generate_url(invite.hash_token),
                      "EMail sender <jobmwaniki18@gmail.com>",
                      [email])
            invite.save()
            return redirect('/dishi/chef/')
    context = {"invite_form": invite_form}
    return render(request, "invite.html", context=context)


def generate_url(str_token):
    url = "http://127.0.0.1:8000/dishi/accounts/"
    return "{}{}".format(url, str_token)
"""
