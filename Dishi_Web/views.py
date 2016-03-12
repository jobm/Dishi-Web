from django.shortcuts import render


def landing_page(request):
    context = {'user': request.user}
    return render(request, "index.html", context=context)
