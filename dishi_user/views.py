from django.shortcuts import render, redirect
from .forms import UserForm
from django.template import RequestContext


# define your views here
# landing page
def landing_page(request):
    context = RequestContext(request)
    return render(request, "index.html", context=context)


# view to render the completion form
def show_user_form(request):
    user_form = UserForm(instance=request.user)
    context = {"user_form": user_form}
    return render(request, "user_registration_form.html", context=context)


# view to complete user registration
def user_registration(request):
    user_form = UserForm(request.POST or None, instance=request.user)
    if request.method == 'POST':
        if user_form.is_valid():
            user_form.save()
            return redirect('/')
    return render(request, "user_registration_form.html",
                  context={"user_form": user_form})


