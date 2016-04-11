from django.shortcuts import render
from django.template import RequestContext


def landing_page(request):
    context = RequestContext(request)
    return render(request, "index.html", context=context)

