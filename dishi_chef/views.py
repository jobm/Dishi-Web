from django.shortcuts import render
from .forms import KitchenForm
# Create your views here.

"""def kitchen(request):
    form = KitchenForm(request.POST or None)

    context = {
        "form": form,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    return render(request, "index.html", context)"""

def Chef (request):
	form = ChefForm(request.POST or None, request.FILES or None)
	context={
	"chef_form":form,
	}
	if form.is_valid():
		instance =form.save(commit=False)
		instance.save()

	return render(request,"index.html",context)
