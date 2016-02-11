from django.shortcuts import render


# Create your views here.
def kitchen_home(request):
    return render(request, "kitchen_layout.html")
