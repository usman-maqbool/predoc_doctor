from django.urls import path

from .views import AbooutPageView, AllPatientView, DashBoardPageView, DisAgrePageView, LandingPageView, PdfPageView,  PrivacyPolicyPageView,ContactUsPageView, StartHerePageView, TermsAndCondtionPageView
#,  show_plates

urlpatterns = [
    path('',LandingPageView.as_view(),name='landing'),
    path('contactus/',ContactUsPageView.as_view(),name='contactus'),
    path('dashboard/',DashBoardPageView.as_view(),name='dashboard'),
    path('start/here/',StartHerePageView.as_view(),name='start_here'),
    path('about/us/',AbooutPageView.as_view(),name='about_us'),
    path('terms/condition/',TermsAndCondtionPageView.as_view(),name='terms_condition'),
    path('privacy/policy/',PrivacyPolicyPageView.as_view(),name='privacy_policy'),
    path('pdf/file/',PdfPageView.as_view(),name='pdf_file'),
    path('disagree/',DisAgrePageView.as_view(),name='disagree'),
    path('all-patient/<int:id>/',AllPatientView.as_view(),name='all_patient'),
]

