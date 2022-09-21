from .models import Appoinment
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


# Create your views here.

class LandingPageView(View):
    def get(self,request):
        context={
            "title":'Landing'
        }
        return render(request, 'landing.html',context)

class ContactUsPageView(View):
    def get(self,request):
        context={
            "title":"Contat Us"
        }

        return render(request, 'contact_us.html', context)



class DashBoardPageView(LoginRequiredMixin,View):
    def get(self,request):
        # patients = Patient.objects.all()
        appoinments = Appoinment.objects.all()

        context={
            "title":"Dashboard",
            "appoinments":appoinments
        }
        messages.success(request,'User Successfully Logged In')
        return render(request,'dashboard.html', context)



class StartHerePageView(LoginRequiredMixin,View):
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

class AbooutPageView(View):
    def get(self,request):
        context = {
            "title":"About"
        }

        return render(request, 'pages/aboutview.html' ,context)