from django.db import models
from django import forms
from firstapp.models import BlogAppUser, BlogPost

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = BlogAppUser
        #fields = "__all__"
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'contact', 'password', 'profile_image')


# login form
class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = BlogAppUser
        fields = ('email', 'password')

#__all__ --> generates form of all fields given in the model
# selective field --> we need to define tuple
# eg: 
#   fields = ('first_name', 'middle_name', 'last_name', 'emial', 'contact', 'profile_image' )

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('post_title', 'post_description', 'slug', 'post_status', 'post_image')