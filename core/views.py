from multiprocessing import context
import re
from turtle import title
from django.shortcuts import render
from django.views import View
# Create your views here.

class LandingPageView(View):
    def get(self,request):
        context={
            "title":'Landing'
        }
        return render(request, 'landing.html',context)




class LogInPageView(View):
    def get(self,request):
        context={
            "title":"LogIn"
        }
        return render(request, 'accounts/login.html' ,context)


class SignUpPageView(View):
    def get(self,request):
        context={
            "title":"SignUp"
        }
        return render(request, 'accounts/sign_up.html', context)

class ResetPasswordPageView(View):
    def get(self,request):
        context={
            "title":"Reset Password"
        }

        return render(request , 'accounts/reset_password.html', context)


class ContactUsPageView(View):
    def get(self,request):
        context={
            "title":"Contat Us"
        }

        return render(request, 'contact_us.html', context)


class DashBoardPageView(View):
    def get(self,request):
        context={
            "title":"Dashboard"
        }

        return render(request,'dashboard.html', context)



class StartHerePageView(View):
    def get(self,request):
        context = {
            "title":"Start Here"
        }
        return render(request, 'start_here.html' , context)


class TermsAndCondtionPageView(View):
    def get(self,request):
        context={
            "title":"Terms and Condition"
        }

        return render(request, 'terms_condition.html', context)


class PrivacyPolicyPageView(View):
    def get(self,request):
        context = {
            "title":"Privacy Policy"
        }

        return render(request, 'privacy_policy.html', context)



class SampleView(View):
    def get(self,request):
      

        return render(request, 'sample.html',{})