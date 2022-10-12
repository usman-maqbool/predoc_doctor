from account.models import UserModel
from .models import Appoinment, QrCode, Questionire
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator ,EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

import io   
import qrcode.image.svg 
import qrcode
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
    def get(self,request, *args, **kwargs):
        obj = Appoinment.objects.first()
        appoinments = Appoinment.objects.all()
        paginator  = Paginator(appoinments,5)
        page       = request.GET.get('page')
        try:
            cr_page = paginator.get_page(page)
        except PageNotAnInteger:
            cr_page = paginator.page(1)
        except EmptyPage:
            cr_page = paginator.page(paginator.num_pages)

        context={
            "title":"Dashboard",
            "appoinments":appoinments,
            'pages':cr_page,
            "obj":obj,
           
        }
        return render(request,'dashboard.html', context)

 
    def post(self, request):
        user = get_object_or_404(UserModel, id=request.user.id)
        user.is_agree = True
        user.save()  # 🖘 save the update in the database
        return redirect('dashboard')

class StartHerePageView(LoginRequiredMixin,View):
    def get(self,request):
        qr_code = QrCode.objects.filter(user=request.user).last()
        context = {
            "title":"Start Here",
            "qr_code":qr_code
        }
        return render(request, 'start_here.html' , context)

    def post(self,request):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        QrCode.objects.create(
            user=request.user,
            first_name=first_name,
            last_name=last_name
            )
        return redirect('start_here')


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






class AllPatientView(View):
    def get(self,request, *args, **kwargs):
        id = kwargs.get('id')
        appoinments = get_object_or_404(Appoinment, id=id)
        context={
            "appoinments":appoinments,
        }
        return render(request,'pages/all_patiebt.html', context)

import datetime as dt
import json
from secrets import compare_digest

from django.conf import settings
from django.db.transaction import atomic, non_atomic_requests
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone

@csrf_exempt
def webhook(request):
    if request.method =='POST':
        print(request.body)
    
    # given_token = request.headers.get("Acme-Webhook-Token", "")
    # if not compare_digest(given_token, settings.ACME_WEBHOOK_TOKEN):
    #     return HttpResponseForbidden(
    #         "Incorrect token in Acme-Webhook-Token header.",
    #         content_type="text/plain",
    #     )

    # Questionire.objects.filter(
    #     received_at__lte=timezone.now() - dt.timedelta(days=7)
    # ).delete()
        payload = json.loads(request.body)
        # x = json.(payload)
        # print("Before load :",type(x))
        

        b =Questionire.objects.create(
            syptoms=payload,
        )
        print("load the body:",b.syptoms['event_id'])
    return render(request, 'pages/questionire.html',content_type="text/plain")