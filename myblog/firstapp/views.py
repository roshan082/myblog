from django.shortcuts import redirect, render
from firstapp.forms import PostCreateForm, UserLoginForm, UserRegisterForm
from firstapp.models import BlogAppUser, BlogPost


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

    else:
        return render(request, template, context)

def post_create(request):
    template = "posts/create.html"
    post_form = PostCreateForm
    context = {'form': post_form}
    if request.method == 'POST':
        obj_post = BlogPost()
        obj_post.post_title = request.POST.get('post_title')
        obj_post.post_description = request.POST.get('post_description')
        obj_post.post_image = request.POST.get('post_image')
        obj_post.post_status = request.POST.get('post_status')
        obj_post.slug = request.POST.get('slug')
        obj_post.save()

        context.setdefault('success', 'Successfully Added !!')
        return render(request, template, context)
    else:
        return render(request, template, context)

def post_index(request):
    if request.session.has_key('session_email'):
        template = "posts/index.html"
        posts = BlogPost.objects.all() # this all() function returns all created posts from database
        context = {'posts': posts}
        return render(request, template, context)
    else:
        form = UserLoginForm
        context = {
            'form' : form,
            'error_msg' : 'Access Forbidden. First Login to the system.'
        }
        template = "users/login.html"
        return render(request, template, context)

def post_edit(request, post_id):
    if request.session.has_key('session_email'):
        template = "posts/edit.html"
        post = BlogPost.objects.get(id=post_id)
        context = {'post': post}
        return render(request, template, context)
    else:
        form = UserLoginForm
        context = {
            'form' : form,
            'error_msg' : 'Edit Access Forbidden. First Login to the system.'
        }
        template = "users/login.html"
        return render(request, template, context)

def post_show(request, post_id):
    if request.session.has_key('session_email'):
        template = "posts/show.html"
        post = BlogPost.objects.get(id=post_id)
        context = {'post': post}
        return render(request, template, context)
    else:
        form = UserLoginForm
        context = {
            'form' : form,
            'error_msg' : 'Access Forbidden. First Login to the system.'
        }
        template = "users/login.html"
        return render(request, template, context)

def post_update(request):
    if request.session.has_key('session_email'):
        template = "posts/edit.html"
        post_form = PostCreateForm
        context = {'form': post_form}
        if request.method == 'POST':
            obj_post = BlogPost.objects.get(id=request.POST.get('post_id'))
            obj_post.post_title = request.POST.get('post_title')
            obj_post.post_description = request.POST.get('post_description')
            obj_post.post_image = request.POST.get('post_image')
            obj_post.post_status = request.POST.get('post_status')
            obj_post.slug = request.POST.get('slug')
            obj_post.save()

            context.setdefault('success', 'Successfully Updated !!!')
            context.setdefault('post', obj_post)
            return render(request, template, context)
            # return redirect(template)
        else:
            return render(request, template, context)
    else:
        form = UserLoginForm
        context = {
            'form' : form,
            'error_msg' : 'Update Access Forbidden. First Login to the system.'
        }
        template = "users/login.html"
        return render(request, template, context)

def post_delete(request, post_id):
    if request.session.has_key('session_email'):
        template = "/posts/"
        # selecting data by object id to delete from database
        post = BlogPost.objects.get(id=post_id)
        post.delete()

        # selecting all data to return to index
        posts = BlogPost.objects.all()
        context = {'posts' : posts}
        return redirect(template)
    else:
        form = UserLoginForm
        context = {
            'form' : form,
            'error_msg' : 'Delete Access Forbidden. First Login to the system.'
        }
        template = "users/login.html"
        return render(request, template, context)

def post_search(request):
    template = "posts/index.html"
    # apply filter in list
    posts = BlogPost.objects.filter(post_title__startswith = request.POST.get('search'))
    context = {'posts' : posts}
    return render(request, template, context)

def user_show(request, id):
    return render(request)

def user_edit(request, id):
    return render(request)

def user_dashboard(request):
    if request.session.has_key('session_email'):
        template = "index.html"
        context = {'success_msg' : 'Welcome ' + request.session['session_email']}
        return render(request, template, context)
    else:
        form = UserLoginForm
        context = {
            'form' : form,
            'error_msg' : 'Access Forbidden. First Login to the system.'
        }
        template = "users/login.html"
        return render(request, template, context)

def user_login(request):
    form = UserLoginForm
    if request.method == "POST":
        try:
            users = BlogAppUser.objects.get(email=request.POST.get('email'))
            if request.POST.get('password') == users.password:
                template = "index.html"
                # storing seession with session key 'session_email'
                request.session['session_email'] = users.email

                # checking session key-value
                if request.session.has_key('session_email'):
                    
                    # accessing session data
                    context = {
                        'success_msg' : 'Welcome ' + request.session['session_email']
                    }
                    return render(request, template, context)
                else:
                    context = {
                        'form': form,
                        'error_msg': 'Access Forbidden'
                    }
                    template = "users/login.html"
                    return render(request, template,context)
            else:
                context = {
                    'form': form,
                    'error_msg': 'Invalid Email or Password'
                }
                template = "users/login.html"
                return render(request, template, context)
        except:
            context = {
                'form' : form,
                'error_msg' : 'Not registered yet...'
                }
            template = "users/login.html"
            return render(request, template, context)
    else:
        context = {'form' : form }
        template = "users/login.html"
        return render(request, template, context)

def user_logout(request):
    if request.session.has_key('session_email'):
        # destroying the session in order to logout user from the system
        del request.session['session_email']
        form = UserLoginForm
        context = {
            'form' : form,
            'error_msg' : 'You are logged out of the system..'
        }
        template = "users/login.html"
        return render(request, template, context)
