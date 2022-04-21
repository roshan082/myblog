# path() --> takes 3 parameter
# 1. urls --> "<url_name/>"
# 2. views and function name --> <views.function_name>
# 3. name --> name = "<url_name>" -- this is optional


from django.urls import path, include
from . import views

urlpatterns = [
    path('demo/',views.demo, name = 'demo')
]