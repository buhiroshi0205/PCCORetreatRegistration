from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest

from registration.forms import RegistrationForm, PersonFormSet

# Create your views here.
def index(request):
  return redirect('/register/')
  # return HttpResponse('you have successfully connected to the registration page')

def register(request):

  if request.method == 'GET':
    context = {
      'form': RegistrationForm(),
      'formset': PersonFormSet()
    }
    return render(request, 'register.html', context)


  elif request.method == 'POST':
    return HttpResponse('Submitted POST.')
  else:
    return HttpResponseBadRequest('Something went wrong due to client side error.') 