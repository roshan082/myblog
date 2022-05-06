from django.shortcuts import render
from firstapp.forms import UserRegisterForm
from firstapp.models import BlogAppUser


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
    urf = UserRegisterForm
    template = 'users/create.html'
    context = {'form': urf}
    if request.method == 'POST':
        user = BlogAppUser()
        user.first_name = request.POST.get('first_name')
        user.middle_name = request.POST.get('middle_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.contact = request.POST.get('contact')
        user.password = request.POST.get('password')
        user.profile_image = request.POST.get('profile_image')
        user.save()

        context.setdefault('success', 'Congratulation your data are registerd successfully !!!')
        
        return render(request, template, context)
        # context = {
        #     'first_name': first_name,
        #     'middle_name': middle_name,
        #     'last_name': last_name,
        #     'email': email,
        #     'contact': contact,
        #     'password': password
        # }

    else:
        return render(request, template, context)