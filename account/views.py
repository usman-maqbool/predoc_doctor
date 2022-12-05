from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import BadHeaderError, EmailMessage, send_mail
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import View

from .forms import ForgetPasswordForm, LoginForm, SignUpForm
from .models import InvitedDoctor, UserModel
from .sendemail import BASE_LINK_FOR_EMAIL, account_activation_token


class SignUpView(View):
    form_class = SignUpForm()
    template_name = 'accounts/sign_up.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request, f"Your login appears to be done.")  
            return redirect("login")
        context = {
            "is_header": "header",
            "form":SignUpForm(),
            'title':"SignUp"
        }
        return render(request, "accounts/sign_up.html", context=context)

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        user_obj = UserModel.objects.filter(email=email).exists()
        invited_user = InvitedDoctor.objects.filter(email=email,is_active = True).exists()
        if invited_user:
            if user_obj:
                messages.info(
                    request,
                    f"The e-mail address you entered is {email} in use, you can try another e-mail address, if the e-mail address belongs to you, you can try to log in..",
                )  
                return redirect("sign_up")
            if password1 == password2:
                user = UserModel.objects.create(
                    username=username,
                    email=email,
                    password=password1,
                )
                user.set_password(password1)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                email_body = {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                }
                link = reverse('activate', kwargs={
                                'uidb64': email_body['uid'], 'token': email_body['token']})
                email_subject = 'Activate your account'
                activate_url = BASE_LINK_FOR_EMAIL+link
                email = EmailMessage(
                        email_subject,
                        f'''Hi {user.email.split('@')[0].capitalize()}., 
Please use the link below to activate your account.
{activate_url}
Thanks 
PreDoc

''',
                        'no-reply@predoc.com.au',
                        [email],
                        )
                email.send(fail_silently=False)
            else:
                messages.error(request, "password is not matching")
                return redirect("sign_up")
            return redirect("verify")
        messages.error(request, "Unfortunately, only selected users can register at this time. Please check back later.")
        return redirect("sign_up")

class VerificationEmailView(View):
    def get(self,request, *args, **kwargs):
        context={
            'title': "Generate Password"
        }
        return render(request, 'accounts/verificationemail.html', context)

class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user = UserModel.objects.get(pk=id)
            if not account_activation_token.check_token(user, token):
                messages.info(request, 'Account is already activated')    
                return redirect('login')
            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()
            messages.success(request, 'Account activated successfully')
            return redirect('login')
        except Exception as ex:
            pass
        return redirect('login')

class LogInView(View):
    def get(self, request, *args, **kwargs ):
        context={
            "title":"LogIn",
            'loginform':LoginForm,
        }
        return render(request, 'accounts/login.html' ,context)

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or passwords")
            return redirect('login')

class LogOutView(View):
    def get(self,request):
        logout(request)
        messages.info(request, 'Sucessfully logged out')
        return redirect('login')

def password_reset_request(request, *args, **kwargs):
	if request.method == "POST":
		password_reset_form = ForgetPasswordForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = UserModel.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "accounts/reset_email.txt"
					c = {
					"email":user.email,
					# 'domain':'127.0.0.1:8000',
					'domain':'https://predoc.com.au',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'no-reply@predoc.com.au' , [user.email], fail_silently=False)
					except BadHeaderError:
						messages.error (request,'Inavlid email')
					return redirect ("reset_password_done")
	password_reset_form = ForgetPasswordForm()
	return render(request, "accounts/forget_password.html", context={"password_reset_form":password_reset_form, 'title':"Reset Password"})

class ResetPasswordDoneView(View):
    def get(self, request):
        context = {
            "title":"Rest Password Done"
        }
        return render(request, 'accounts/reset-password-done.html',context)

class ResetPasswordConfirmView(View):
    def get(self,request, *args, **kwargs):
        context={
            'title': "Generate Password"
        }
        messages.success(request,'Your Password is successfully reset')
        return render(request, 'accounts/password_reset_confirm.html', context)
