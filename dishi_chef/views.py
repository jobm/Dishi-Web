from django.shortcuts import render, redirect
from dishi_chef.forms import KitchenForm, InviteForm


# Create your views here.
def kitchen_home(request):
    return render(request, "kitchen.html")


# kitchen form view
def kitchen_form_view(request):
    kitchen_form = KitchenForm(request.POST or None)
    context = {"kitchen_form": kitchen_form}
    return render(request, "kitchen_reg_form.html", context=context)


# view to send an invite
def invite_team(request):
    invite_form = InviteForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        if invite_form.is_valid():
            email = invite_form.cleaned_data.get('recepient_email')
            print(email)
            return redirect('/dishi/chef/')
    context = {"invite_form": invite_form}
    return render(request, "invite.html", context=context)
