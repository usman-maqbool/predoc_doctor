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
        qr_code = QrCode.objects.filter(user=request.user).first()
        context = {
            "title":"Start Here",
            "qr_code":qr_code
        }
        return render(request, 'start_here.html' , context)

    def post(self,request):
        # first_name=request.POST['first_name']
        # last_name=request.POST['last_name']
        url=request.POST['url']
        print(url)
        QrCode.objects.create(
            user=request.user,
            # first_name=first_name,
            # last_name=last_name,
            url=url
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


@csrf_exempt
def webhook(request):
    if request.method =='POST':
        # print(request.body)
        payload = json.loads(request.body)
        json_object = json.dumps(payload)
        print('finding type',type(json_object))        




        # jsondata = request.body
        # data = json.loads(jsondata)
        # for answer in data['form_response']['answers']: # go through all the answers
        #     type = answer['type']
        #     print(f'answer: {answer[type]}') # print value of answers



        

        # print("i am finding thetype",type(answer))
        # print(answer)
       
        # Questionire.objects.create(
        #     syptoms=payload,
            # syptoms=answer,
            # syptoms=json_object,
            # print("load the body:",payload['form_response'])
        # )
    return render(request, 'pages/questionire.html',content_type="text/plain")