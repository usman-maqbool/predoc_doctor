
from account.forms import ContactForm, SignUpForm
from account.models import UserModel
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import BadHeaderError, send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import get_template
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from qrcode import *
from xhtml2pdf import pisa
from .utils import webhookSignature
from .models import Appoinment, QrCode
import json
from .parser import Parser





class LandingPageView(View):
    def get(self, request):
        context={
            "title":'Landing'
        }
        return render(request, 'landing.html', context)

class DashBoardPageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        obj = Appoinment.objects.last()

        appoinments = Appoinment.objects.all().order_by("-created_at")
        paginator  = Paginator(appoinments,5)
        page       = request.GET.get('page')
        try:
            cr_page = paginator.get_page(page)
        except PageNotAnInteger:
            cr_page = paginator.page(1)
        except EmptyPage:
            cr_page = paginator.page(paginator.num_pages)
        
       
        parser = Parser(payload=obj.questions)
        refactored_payload = zip(parser.parse_questions(), parser.parse_answers())
        popupp_payload = parser.parse_original_questionnaire()
        context={
            'refactored_payload':refactored_payload,
            'popupp_payload':popupp_payload,
            "title":"Dashboard",
            'pages':cr_page,
            "obj":obj,
            "dob":parser.get_date_of_birth(),
            "age": parser.get_age(),
            "first_name": parser.get_first_name(),
        }

        return render(request,'dashboard.html', context)

    def post(self, request):
        user = get_object_or_404(UserModel, id=request.user.id)
        user.is_agree = True
        user.save()
        return redirect('dashboard')

class WaitingRoomView(LoginRequiredMixin, View):
    def get(self, request):
        qr_code = QrCode.objects.filter().last()
        update_id = get_object_or_404(UserModel, id = request.user.id)
        update_form = SignUpForm(instance = update_id)
        
        context = {
            "title":"Waiting Room",
            "qr_code":qr_code,
            "update_form":update_form
        }
        return render(request, 'waiting_room.html', context)

    def post(self, request):
        first_name   = request.POST.get("first_name") 
        last_name    = request.POST.get("last_name") 
        user  = get_object_or_404(UserModel,id=request.user.id)
        user.first_name = first_name
        user.last_name  = last_name
        user.save()
        messages.success(request, "first_name and last_name updated successfully")
        return redirect ("start_here")

class OnlyQrCodeView(View):
    def get(self, request):
        qr_code = QrCode.objects.filter().last()
        update_id=get_object_or_404(UserModel, id = request.user.id)
        update_form = SignUpForm(instance = update_id)
        context = {
            "title":"Qr Code",
            "qr_code":qr_code,
            "update_form":update_form
        }
        return render(request, 'pages/only_qrcode.html', context)

    def post(self, request):
        first_name   = request.POST.get("first_name") 
        last_name    = request.POST.get("last_name") 
        user  = get_object_or_404(UserModel,id=request.user.id)
        user.first_name = first_name
        user.last_name  = last_name
        user.save()
        messages.success(request, "first_name and last_name updated successfully")
        return redirect ("only_qrcode")

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
        logout(request)
        context = {
            'title':"Disagree"
        }
        return render(request, 'pages/disagree.html', context)

class AllPatientView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        appoinments = get_object_or_404(Appoinment, id=id)
        # refactored_payload = zip(appoinments.qs.syptoms['form_response']['definition']['fields'],appoinments.qs.syptoms['form_response']['answers'])
        parser = Parser(payload=appoinments.questions)
        refactored_payload = zip(parser.parse_questions(), parser.parse_answers())
        popupp_payload = parser.parse_original_questionnaire()
        context={
            "appoinments":appoinments,
            "refactored_payload":refactored_payload,
            'popupp_payload':popupp_payload,
        }
        return render(request, 'pages/all_patiebt.html', context)

@csrf_exempt
def webhook(request):
    if request.method =='POST':
        print(request.META ,  ':::::::::::::::::::')

        receivedSignature = request.META.get("HTTP_TYPEFORM_SIGNATURE")
        print(receivedSignature,"::::::::::::::::::::::::;;")
        
        if receivedSignature is None:
            return Exception(403, detail="Permission denied.")
            
        sha_name, signature = receivedSignature.split('=', 1)
        if sha_name != 'sha256':
            return Exception(501, detail="Operation not supported.")
        

        is_valid = webhookSignature(signature, request.body)
        # raw
        if(is_valid != True):
            return Exception(403, detail="Invalid signature. Permission Denied.")

        response = request.body.decode()
        payload = json.loads(response)

        Appoinment.objects.create(
            questions = payload
        )
    return render(request, 'pages/questionire.html', context={} )

def get_qr_pdf(request):
    template_path = 'pages/pdf_click.html'
    qr_code = QrCode.objects.filter().first()
    user = get_object_or_404(UserModel, id = request.user.id)
    context = {'qr_image': qr_code,'user':user}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="predoc.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response
    )
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

class ContactUsPageView(View):
    def get(self, request):
        form = ContactForm()
        context={
            "title":"Contat Us",
            'form':form
        }
        return render(request, 'contact_us.html', context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Contact Form" 
            body = {
                'name': form.cleaned_data['name'], 
                'email': form.cleaned_data['email'], 
                'type': form.cleaned_data['type'], 
                'message':form.cleaned_data['message'], 
                }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, f'{request.user}', ['admin@example.com']) 
            except BadHeaderError:
                messages.error(request,'Something getting wrong')
                return redirect('contactus')
            messages.success(request,'Your message is successfully sent. we will contact you soon..!')
            return redirect ("contactus")

