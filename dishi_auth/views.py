from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext

# Create your views here.
def auth_home(request):
    return render(request, 'index.html')


def home(request):
   context = RequestContext(request,
                           {'user': request.user})
   return render_to_response('auth.html',
                             context_instance=context)