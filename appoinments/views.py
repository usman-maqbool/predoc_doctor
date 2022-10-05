from account.models import UserModel
from .models import Appoinment
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator ,EmptyPage, PageNotAnInteger

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

# class DashBoardPageView(LoginRequiredMixin,View):
#     def get(self,request):
#         appoinments = Appoinment.objects.all()
#         obj = Appoinment.objects.first()

#         context={
#             "title":"Dashboard",
#             "appoinments":appoinments,
#             "obj":obj
#         }
#         return render(request,'dashboard.html', context)


class DashBoardPageView(LoginRequiredMixin,View):
    def get(self,request):
        obj = Appoinment.objects.first()
        appoinments = Appoinment.objects.all()
        
        # pages = Paginator(appoinments,5)
        # page_number = request.GET.get('page')
        # # try:
        # #     page_obj = pages.get_page(page_number)
        # # except PageNotAnInteger:
        # #     page_obj = pages.page(1)
        # # except EmptyPage:
        # #     page_obj = pages.page(pages.num_pages)

        paginator  = Paginator(appoinments,5)
        page       = request.GET.get('page')
        # cr_page = paginator.get_page(page)
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
            "obj":obj
        }
        return render(request,'dashboard.html', context)

    # def post(self, request, *args, **kwargs):
    #     id = kwargs.get('id')
    #     check = get_object_or_404(UserModel, id = id)
    #     check.is_agree = True
    #     check.save()
    #     return redirect('dashboard')
    
    # def ticket_system_view(request, id):
    #     check = get_object_or_404(UserModel, id=id)
    #     if request.method == 'POST':
    #         check.is_agree = True
    #         check.save()  # 🖘 save the update in the database
    #         return redirect('dashboard', id=id)

    #     return render(request, 'dashboard.html', {'check': check})
    #     # return render(request,'dashboard.html', context)

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



class AllPatientView(View):
    def get(self,request, *args, **kwargs):
        id = kwargs.get('id')
        appoinments = get_object_or_404(Appoinment, id=id)
        context={
            "appoinments":appoinments,
        }
        return render(request,'pages/all_patiebt.html', context)