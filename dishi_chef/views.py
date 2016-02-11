from django.shortcuts import render, redirect
# from dishi_chef.forms import KitchenForm, InviteForm
# from dishi_chef.models import Invite
from django.core.mail import send_mail


# Create your views here.
def kitchen_home(request):
    return render(request, "kitchen.html")


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
