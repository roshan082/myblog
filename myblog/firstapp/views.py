from django.shortcuts import render

# Create your views here.
def demo(request): # request parameter is mandatory in every function in django because this is a client site application.
    templates = 'index.html'
    return render(request, templates)
    # http response --> 

# render() -> takes three parameter
# 1. request
# 2. template
# 3. context/data (must be in the dict) -> optional
