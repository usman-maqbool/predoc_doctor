from django.urls import path

from .views import AbooutPageView, DashBoardPageView, LandingPageView,  PrivacyPolicyPageView,ContactUsPageView, StartHerePageView, TermsAndCondtionPageView

urlpatterns = [
    path('',LandingPageView.as_view(),name='landing'),
    path('contactus/',ContactUsPageView.as_view(),name='contactus'),
    path('dashboard/',DashBoardPageView.as_view(),name='dashboard'),
    path('start/here/',StartHerePageView.as_view(),name='start_here'),
    path('about/us/',AbooutPageView.as_view(),name='about_us'),
    path('terms/condition',TermsAndCondtionPageView.as_view(),name='terms_condition'),
    path('privacy/policy',PrivacyPolicyPageView.as_view(),name='privacy_policy'),
]

