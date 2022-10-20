from account.models import UserModel
from .models import Appoinment, QrCode, Questionire
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator ,EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.csrf import csrf_exempt
from qrcode import *
import time
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib import messages
from account.forms import SignUpForm
class LandingPageView(View):
    def get(self, request):
        context={
            "title":'Landing'
        }
        return render(request, 'landing.html', context)

class ContactUsPageView(View):
    def get(self, request):
        context={
            "title":"Contat Us"
        }
        return render(request, 'contact_us.html', context)

class DashBoardPageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
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
    def get(self, request):
        # qr_code = QrCode.objects.filter(user=request.user).first()
        qr_code = QrCode.objects.filter().first()
        update_id=get_object_or_404(UserModel, id = request.user.id)
        update_form = SignUpForm(instance = update_id)
        
        context = {
            "title":"Start Here",
            "qr_code":qr_code,
            "update_form":update_form
        }
        return render(request, 'start_here.html', context)

    def post(self, request):
        first_name   = request.POST.get("first_name") 
        last_name    = request.POST.get("last_name") 
       
        user  = get_object_or_404(UserModel,id=request.user.id)


        user.first_name = first_name
        user.last_name  = last_name
     
        user.save()
        # if user:

            # messages.success (request,"User has been updated")
        return redirect ("start_here")
        
        
        
        
        
        # # first_name = request.POST['first_name']
        # # last_name = request.POST['last_name']
        
        # id = request.user.id
        # update_id=get_object_or_404(UserModel, id = id)
        # print(id, 'its id')
        # update_form = SignUpForm(request.POST or None, instance=update_id)
        # if update_form.is_valid():
        #     update_form.save()
        #     # obj.save()
        #     return redirect('start_here')
            
        # else:
        #     print(request.POST)
        #     return redirect('start_here')


        # data = request.POST['url']
        # img = make(data)
        # img_name = 'qr' + str(time.time()) + '.png'
        # img.save(img_name)
        # QrCode.objects.create(
        #     user=request.user,
        #     first_name=first_name,
        #     last_name=last_name,
        #     # url=data,
        #     image=img_name
        #     )
        # messages.success(request,'Qr Code created succesfully..!')
        # return redirect('start_here')

class TermsAndCondtionPageView(View):
    def get(self, request):
        context={
            "title":"Terms and Condition"
        }
        return render(request, 'terms_condition.html', context)

class PrivacyPolicyPageView(View):
    def get(self, request):
        context = {
            "title":"Privacy Policy"
        }
        return render(request, 'privacy_policy.html', context)

class AbooutPageView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            "title":"About"
        }
        return render(request, 'pages/aboutview.html', context)

class DisAgrePageView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'title':"Disagree"
        }
        return render(request, 'pages/disagree.html', context)

class AllPatientView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        appoinments = get_object_or_404(Appoinment, id=id)
        refactored_payload = zip(appoinments.qs.syptoms['form_response']['definition']['fields'],appoinments.qs.syptoms['form_response']['answers'])
        context={
            "appoinments":appoinments,
            "refactored_payload":refactored_payload
        }
        return render(request,'pages/all_patiebt.html', context)

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


def get_qr_pdf(request):
    template_path = 'pages/pdf_click.html'
    qr_code = QrCode.objects.filter().first()
    id = request.user.id
    user = get_object_or_404(UserModel, id = id)
    context = {'qr_image': qr_code,'user':user}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="predoc.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response