from django.http import HttpResponse

from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth import get_user_model
from .forms import SignUpForm 
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.models import auth
User = get_user_model()

# Create your views here.


class LogInPageView(View):
    def get(self,request):
        context={
            "title":"LogIn"
        }
        return render(request, 'accounts/login.html' ,context)

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Invalid UserName or Password')
            return redirect('login')


class SignUpPageView(SuccessMessageMixin,CreateView):
    form_class = SignUpForm
    success_url ='/account/login/'   
    success_message = "User Succesfully Registerd"
    template_name = 'accounts/sign_up.html'




class LogOutPageView(View):
    def get(self,request):
        logout(request)
        messages.info(request, 'You Sucessfully logged out')
        return redirect('login')




# def register_view(request,*args,**kwargs):
#     user = request.user
#     if user.is_authenticated:
#         return HttpResponse(f"you are already authenticated a {user.email}")
#     context = {

#     }
#     if request.POST:
#         form = RegistrationForm(request.POST)
#         print(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email').lower()
#             password1 = form.cleaned_data.get('password1')
#             account = authenticate(email=email, password = password1)
#             login(request,account)
#             return redirect('login')
#         else:
#             return redirect('register')
#     return render(request, 'accounts/register.html', context)


# class LoginView(View):

#     def get(self,request):


#         context ={
#             'loginform':LoginForm
#         }

#         return render(request, 'registration/login.html', context)

#     def post(self,request):
#         if(request.method == "POST"):
#             email = request.POST.get('email')
#             password = request.POST.get('password')

#             if(email != '' and password != ''):
#                 user = auth.authenticate(email=email, password=password ) 

#                 if user is not None: 
#                     request.session['email'] = email
#                     auth.login(request, user)
#                     request.session.set_expiry(10000)
#                     data={}
#                     data['success_message'] ='Successfully login'
#                     return redirect('dashboard')
#                 else:
                   
#                     messages.error(request, "Invalid Credentials ")
#                     return redirect('account:login')
#             else:
#                 messages.error(request, "Some field is empty")
#                 return redirect('account:login')
#         else:
#             return redirect('account:login')
