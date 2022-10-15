from account.models import UserModel
from .models import Appoinment, QrCode, Questionire
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator ,EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from qrcode import *
import time

class LandingPageView(View):
    def get(self,request):
        context={
            "title":'Landing'
        }
        return render(request, 'landing.html', context)

class ContactUsPageView(View):
    def get(self,request):
        context={
            "title":"Contat Us"
        }
        return render(request, 'contact_us.html', context)

class DashBoardPageView(LoginRequiredMixin, View):
    def get(self,request, *args, **kwargs):
        obj = Appoinment.objects.first()
        refactored_payload = zip(obj.qs.syptoms['form_response']['definition']['fields'],obj.qs.syptoms['form_response']['answers'])

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
            "refactored_payload":refactored_payload,
        }
        return render(request,'dashboard.html', context)

    def post(self, request):
        user = get_object_or_404(UserModel, id=request.user.id)
        user.is_agree = True
        user.save()  # 🖘 save the update in the database
        return redirect('dashboard')

class StartHerePageView(LoginRequiredMixin, View):
    def get(self,request):
        qr_code = QrCode.objects.filter(user=request.user).first()
        context = {
            "title":"Start Here",
            "qr_code":qr_code
        }
        return render(request, 'start_here.html', context)

    def post(self,request):
        data = request.POST['url']
        img = make(data)
        img_name = 'qr' + str(time.time()) + '.png'
        img.save(img_name)
        QrCode.objects.create(
            user=request.user,
            url=data,
            image=img_name
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

class AbooutPageView(LoginRequiredMixin, View):
    def get(self,request):
        context = {
            "title":"About"
        }
        return render(request, 'pages/aboutview.html', context)

class PdfPageView(LoginRequiredMixin, View):
    def get(self,request):
        context={
            'title':"Pdf File"
        }
        return render(request, 'pages/pdf_click.html', context)

class DisAgrePageView(LoginRequiredMixin, View):
    def get(self,request):
        context = {
            'title':"Disagree"
        }
        return render(request, 'pages/disagree.html', context)

class AllPatientView(View):
    def get(self,request, *args, **kwargs):
        id = kwargs.get('id')
        appoinments = get_object_or_404(Appoinment, id=id)
        refactored_payload = zip(appoinments.qs.syptoms['form_response']['definition']['fields'],appoinments.qs.syptoms['form_response']['answers'])
        context={
            "appoinments":appoinments,
            "refactored_payload":refactored_payload
        }
        return render(request,'pages/all_patiebt.html', context)


# @csrf_exempt
# def webhook(request):
#     if request.method =='POST':
#         response = request.body.decode()
#         payload = json.loads(response)

#         Questionire.objects.create(
#             syptoms=payload,
#         )
        
#     return render(request, 'pages/questionire.html' )


@csrf_exempt
def webhook(request):
    appo = Appoinment.objects.filter().first()
    refactored_payload = zip(appo.qs.syptoms['form_response']['definition']['fields'],appo.qs.syptoms['form_response']['answers'])
    context={
        'title':'TypeForm Response',
        'appo':appo,
        'refactored_payload':refactored_payload
    }
    if request.method =='POST':
        response = request.body.decode()
        payload = json.loads(response)

        Questionire.objects.create(
            syptoms=payload,
        )
        
    return render(request, 'pages/questionire.html', context )

