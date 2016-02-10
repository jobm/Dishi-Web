from django.shortcuts import render


# Create your views here.
def auth_home(request):
    return render(request, 'index.html')
