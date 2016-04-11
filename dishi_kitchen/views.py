from django.shortcuts import render, redirect
from dishi_chef.models import Chef
from dishi_kitchen.models import Kitchen, Follower
from dishi_kitchen.forms import RecipeForm, MenuForm, InviteForm, KitchenForm
from shared_files.dishi_user import (get_object_or_none,
                                     filter_object_or_none,
                                     BUSINESS_TYPE_CHOICES,
                                     KITCHEN_TYPE_CHOICES)
from dishi_kitchen.models import Menu, MenuLike, Recipe, Invite, Conversation
from django.core.mail import send_mail


# url:/dishi/chef/kitchen/
# Create your views here.
def kitchen_home(request, username):
    # check whether the person trying to access the kitchen is the owner of the username
    # used to request for the kitchen, if not just render the kitchen of the requested chef.
    # if the person requesting is the owner of the username, and they are a verified chef,          # create a
    # kitchen for them
    context = {}
    chef = get_object_or_none(Chef, username=username)
    if chef.username == request.user.username:
        kitchen = get_object_or_none(Kitchen, owner=chef)
        if kitchen is None:
            kitchen_form = KitchenForm()
            context = {"kitchen_form": kitchen_form, "chef": chef}
            return render(request, "kitchen_reg_form.html", context=context)
        else:
            context = set_kitchen_context(chef, str(username))
    else:
        if chef is not None:
            kitchen = get_object_or_none(Kitchen, owner=chef)
            followers = Follower.objects.filter(kitchen=kitchen)
            if kitchen is not None:
                if followers is None:
                    context = set_kitchen_context(chef)
                else:
                    context = set_kitchen_context(chef, followers)
    return render(request, "kitchen_layout.html", context=context)


# this is not a view rather a helper method to set the context of a kitchen
def set_kitchen_context(chef, *args):
    kitchen = get_object_or_none(Kitchen, owner=chef)
    menus = filter_object_or_none(Menu, owner=kitchen)
    recipes = filter_object_or_none(Recipe, owner_id=kitchen)
    conversations = filter_object_or_none(Conversation, owner=kitchen)
    followers = Follower.objects.filter(kitchen=kitchen)
    # print([dish for dish in menus][0].likes if not None else "Null")
    k_t = dict(KITCHEN_TYPE_CHOICES)[kitchen.kitchen_type]
    b_t = dict(BUSINESS_TYPE_CHOICES)[kitchen.business_type]
    context = {
        "chef": chef,
        "kitchen": kitchen,
        "dishes": menus,
        "recipes": recipes,
        "conversations": conversations,
        "followers": followers,
        "kitchen_type": k_t,
        "business_type": b_t,
        "owner": args}
    return context


# kitchen save action
def create_kitchen(request, username):
    kitchen_form = KitchenForm(request.POST or None)
    chef = get_object_or_none(Chef, username=username)
    if request.method == 'POST':
        if kitchen_form.is_valid():
            kitchen = kitchen_form.save(commit=False)
            kitchen.owner = chef
            kitchen.save()
            kitchen_form.save_m2m()
            return redirect("/chef/{}/kitchen/".format(username))
    context = {"kitchen_form": kitchen_form, "chef": chef}
    return render(request, "kitchen_reg_form.html", context=context)


# view to edit kitchen details
def edit_kitchen(request, username):
    pass


# view to render a form to add a menu item
# http://localhost:8000/chef/kitchen/{{username}}/menu/
def kitchen_menu(request, username):
    menu_form = MenuForm()
    context = {"menu_form": menu_form, "username": username}
    return render(request, "menu_add_form.html", context=context)


# view to add the menu item
# /chef/kitchen/{{username}}/menu/create/
def add_kitchen_menu(request, username):
    menu_form = MenuForm(request.POST or None)
    chef = get_object_or_none(Chef, username=username)
    kitchen = get_object_or_none(Kitchen, owner=chef)
    if request.method == 'POST':
        if menu_form.is_valid():
            menu = menu_form.save(commit=False)
            menu.owner = kitchen
            menu.save()
            menu_form.save_m2m()
            return redirect("/chef/kitchen/{}/".format(username))
    context = {"menu_form": menu_form, "username": username}
    return render(request, "menu_add_form.html", context=context)


# view to edit a kitchen menu
def edit_kitchen_menu(request, username):
    pass


# view to delete a kitchen menu
def delete_kitchen_menu(request, username):
    pass


# view to like a kitchen menu
def like_kitchen_menu(request, username):
    like = get_object_or_none(MenuLike, liker=request.user)
    if not like:
        like.like += 1
        like.liker = request.user
        like.save()


# view to unlike a kitchen menu
def unlike_kitchen_menu(request, username):
    like = get_object_or_none(MenuLike, liker=request.user)
    if like:
        like.delete()


# view to render a form to add a recipe item
# /chef/kitchen/{{username}}/recipe/
def kitchen_recipe(request, username):
    recipe_form = RecipeForm()
    context = {"recipe_form": recipe_form, "username": username}
    return render(request, "recipe_add_form.html", context=context)


# view to add recipe item
def add_kitchen_recipe(request, username):
    recipe_form = RecipeForm(request.POST or None)
    chef = get_object_or_none(Chef, username=username)
    kitchen = get_object_or_none(Kitchen, owner=chef)
    if request.method == 'POST':
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.owner = kitchen
            recipe.save()
            recipe_form.save_m2m()
            return redirect("/chef/kitchen/{}/".format(username))
    context = {"recipe_form": recipe_form, "username": username}
    return render(request, "recipe_add_form.html", context=context)


# view to edit a kitchen menu
def edit_kitchen_recipe(request, username):
    pass


# view to delete a kitchen menu
def delete_kitchen_recipe(request, username):
    pass


# view to follow a kitchen
def follow_kitchen(request, username):
    chef = get_object_or_none(Chef, username=username)
    kitchen = get_object_or_none(Kitchen, owner=chef)
    if request.user in Follower.objects.filter(kitchen=kitchen):
        follower = Follower(follower=request.user)
        follower.save()
        kitchen.followers.add(follower)
    return redirect("/chef/kitchen/{}/".format(username))


# view to un follow a kitchen
def un_follow_kitchen(request, username):
    f = get_object_or_none(Follower, follower=request.user)
    if f is not None:
        f.delete()
    return redirect("/kitchen/{}/".format(username))


# view to send an invite
def invite_team(request, username):
    invite_form = InviteForm(request.POST or None)
    # context = {}
    invite = Invite()
    if request.method == 'POST':
        if invite_form.is_valid():
            email = invite_form.cleaned_data.get('recipient_email')
            invite.recipient_email = email
            invite.hash_token = invite.generate_unique_hash()
            invite.owner = request.user
            # print(email, invite.hash_token, generate_url(invite.hash_token))
            send_mail("Invite to team", generate_url(invite.hash_token),
                      "EMail sender <dishicommunity@gmail.com>",
                      [email])
            invite.save()
            return redirect('/chef/{}/'.format(username))
    context = {"invite_form": invite_form}
    return render(request, "invite.html", context=context)


def generate_url(str_token):
    url = "http://127.0.0.1:8000/dishi/accounts/"
    return "{}{}".format(url, str_token)


# view to add a post to the kitchen by displaying a post form
def create_a_conversation(request, username):
    pass


# view to save the post
def save_a_conversation(request, username):
    pass


# view to edit a post
def edit_a_conversation(request, username):
    pass


# view to delete a post
def delete_a_conversation(request, username):
    pass
