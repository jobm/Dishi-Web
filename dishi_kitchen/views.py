from django.shortcuts import render
from dishi_kitchen.forms import RecipeForm, MenuForm, InviteForm
from shared_files.dishi_user import get_object_or_none
from dishi_kitchen.models import Menu,Recipe,Invite


# url:  /dishi/chef/kitchen/
# Create your views here.
def kitchen_home(request, username):
    return render(request, "kitchen_layout.html")


# view to render a form to add a menu item
def kitchen_menu(request):
    # menu_item = get_object_or_none(Menu, owner=request.user)
    menu_form = MenuForm()
    return render(request, "menu_add_form.html", context={"menu_form": menu_form})


# view to add the menu item
def add_kitchen_menu(request):
    pass


# view to render a form to add a recipe item
def kitchen_recipe(request):
    pass


# view to add recipe item
def add_kitchen_recipe(request):
    pass


# view to load the blog app
def kitchen_blog(request):
    pass


# kitchen form view
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
