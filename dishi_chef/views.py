from django.shortcuts import render
from dishi_chef.forms import KitchenForm


# Create your views here.
def kitchen_form_view(request):
    kitchen_form = KitchenForm(request.POST or None)
    context = {"kitchen_form": kitchen_form}
    return render(request, "kitchen_reg_form.html", context=context)
