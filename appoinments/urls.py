from django.urls import path
from .views import (
     AbooutPageView,
     OnlyQrCodeView,
     get_qr_pdf,
     AllPatientView, 
     DashBoardPageView, 
     DisAgrePageView, 
     LandingPageView, 
     PrivacyPolicyPageView,
     ContactUsPageView, 
     webhook,
     WaitingRoomView,
     TermsAndCondtionPageView
)

urlpatterns = [
    path('', LandingPageView.as_view(),name='landing'),
    path('contactus/', ContactUsPageView.as_view(),name='contactus'),
    path('dashboard/', DashBoardPageView.as_view(),name='dashboard'),
    path('start/here/', WaitingRoomView.as_view(),name='start_here'),
    path('qr/code/', OnlyQrCodeView.as_view(),name='only_qrcode'),
    path('about/us/', AbooutPageView.as_view(),name='about_us'),
    path('terms/condition/', TermsAndCondtionPageView.as_view(),name='terms_condition'),
    path('privacy/policy/', PrivacyPolicyPageView.as_view(),name='privacy_policy'),
    path('disagree/', DisAgrePageView.as_view(),name='disagree'),
    path('all-patient/<int:id>/', AllPatientView.as_view(),name='all_patient'),
    path('webhhook/', webhook ,name='questionire'),
    path('pdfdown/',get_qr_pdf, name= 'pdfdown')
]

