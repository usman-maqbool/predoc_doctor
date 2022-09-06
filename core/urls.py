from django.urls import path

from .views import DashBoardPageView, LandingPageView, LogInPageView, ResetPasswordPageView,SignUpPageView , ContactUsPageView

urlpatterns = [
    path('',LandingPageView.as_view(),name='landing'),
    path('login/',LogInPageView.as_view(),name='login'),
    path('signup/',SignUpPageView.as_view(),name='sign_up'),
    path('reset/password/',ResetPasswordPageView.as_view(),name='reset_password'),
    path('contactus/',ContactUsPageView.as_view(),name='contactus'),
    path('dashboard/',DashBoardPageView.as_view(),name='dashboard'),
]

