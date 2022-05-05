import re
from django.shortcuts import render
from firstapp.forms import UserRegisterForm


# Create your views here.
def demo(request): # request parameter is mandatory in every function in django because this is a client site application.
    urf = UserRegisterForm
    templates = 'index.html'
    context = {'form' : urf}
    return render(request, templates, context)
    # http response --> 

# render() -> takes three parameter
# 1. request
# 2. template
# 3. context/data (must be in the dict) -> optional

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')

        context = {
            'first_name': first_name,
            'middle_name': middle_name,
            'last_name': last_name,
            'email': email,
            'contact': contact,
            'password': password
        }
    else:
        urf = UserRegisterForm
        template = 'create.html'
        context = {'form': urf}
        return render(request, template, context)