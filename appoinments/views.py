from .models import Appoinment
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


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
        appoinments = Appoinment.objects.all()

        context={
            "title":"Dashboard",
            "appoinments":appoinments,
        }
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

class AbooutPageView(LoginRequiredMixin,View):
    def get(self,request):
        context = {
            "title":"About"
        }
        return render(request, 'pages/aboutview.html' ,context)

class PdfPageView(LoginRequiredMixin,View):
    def get(self,request):
        context={
            'title':"Pdf File"
        }
        return render(request, 'pages/pdf_click.html', context)

class DisAgrePageView(LoginRequiredMixin,View):
    def get(self,request):
        context = {
            'title':"Disagree"
        }
        return render(request, 'pages/disagree.html', context)

# class AllPatientView(View):
#     def get(self,request, *args, **kwargs):
#         # appoinments = Appoinment.objects.all()
#         id = kwargs.get('id')
#         appoinments = get_object_or_404(Appoinment, id=id)
#         print(id,'id is')
#         context={
#             "appoinments":appoinments,
#         }
#         return render(request,'pages/all_patiebt.html', context)


class AllPatientView(View):
    def get(self,request, *args, **kwargs):
        # appoinments = Appoinment.objects.all()
        id = kwargs.get('id')
        appoinments = get_object_or_404(Appoinment, id=id)
        context={
            "appoinments":appoinments,
        }
        return render(request,'pages/all_patiebt.html', context)