from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

from registration.forms import RegistrationForm

# Create your views here.
def index(request):
  return HttpResponse('you have successfully connected to the registration page')

def register(request):
  if request.method == 'GET':
    context = {'form': RegistrationForm()}
    return render(request, 'register.html', context)
  elif request.method == 'POST':
    return HttpResponse('Test successful')
  else:
    return HttpResponseBadRequest('Something went wrong due to client side error.') 