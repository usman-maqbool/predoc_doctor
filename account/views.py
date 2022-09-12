
from multiprocessing import context
from tkinter import E
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth import get_user_model
from .forms import SignUpForm , LoginForm ,RecoverPasswordForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import auth
from .models import UserModel 
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

# from .sendemail import account_activation_token
# from django.utils.encoding import force_text
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
import uuid

from django.contrib.auth.tokens import default_token_generator
# from .sendemail import send_foregt_password_email
User = get_user_model()

# Create your views here.


class LogInPageView(View):
    def get(self,request):

        context={
            "title":"LogIn",
            'loginform':LoginForm

        }
        return render(request, 'accounts/login.html' ,context)

    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
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

class ForgetSuccesFullMessagePAgeView(View):
    def get(self,request):
        context={
            "title":"Success Full Message"
        }

        return render(request , 'accounts/forgot-successfull-message.html', context)
class ResetForgotPasswordPAgeView(View):
    def get(self,request):
        context={
            "title":"Reset Password"
        }

        return render(request , 'accounts/reset_password.html', context)

        
class ForgetPasswordPageView(View):
    template_name = 'accounts/forget_password.html'
    def get(self, request):

        context = {

            'form' :RecoverPasswordForm
        }
        return render(request, 'accounts/forget_password.html', context)

    def post(self,request):
        email = request.POST.get("email", "default value")
        if User.objects.filter(email=email).exists():
            obj = User.objects.filter(email=email)
            for i in obj:
                user_details = {'username':i.username }
                username = user_details['username']
            password_reset_form = RecoverPasswordForm(request.POST)
            if password_reset_form.is_valid():
                data = password_reset_form.cleaned_data['email']
                associated_users = User.objects.filter(Q(email=data))
                if associated_users.exists():
                    for user in associated_users:
                        subject = "Password Reset Requested"
                        email_template_name = "accounts/reset_email.txt"
                        c = {
                            "username": user.username,
                            "email": user.email,
                            'domain': '127.0.0.1:8000',
                            'site_name': 'Website',
                            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                            "user": user,
                            'token': default_token_generator.make_token(user),
                            'protocol': 'http',
                        }
                        email = render_to_string(email_template_name, c)
                        try:
                            send_mail(subject, email, 'admin@example.com',
                            [user.email], fail_silently=False)
                        except BadHeaderError:
                            messages.info(request, "Email Doesn't Exists ")
                            return redirect('forget_password')
                        return redirect("forgot-successfull-message")
                password_reset_form = RecoverPasswordForm()
                return render(request,"accounts/forget_password.html", context={"password_reset_form": password_reset_form})
            else:
                messages.info(request, 'Please Enter Your Email')
                return redirect('accounts/forget_password')
        else:
            messages.info(request, "Email doesn't  exist")
            return redirect('accounts/forget_password')

       
        




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
