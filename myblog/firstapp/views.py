from django.shortcuts import render

from firstapp.forms import UserRegisterForm

# Create your views here.
def demo(request): # request parameter is mandatory in every function in django because this is a client site application.
    urf = UserRegisterForm
    templates = 'index.html'
    context = {
        'form' : urf
    }
    return render(request, templates, context)
    # http response --> 

# render() -> takes three parameter
# 1. request
# 2. template
# 3. context/data (must be in the dict) -> optional
