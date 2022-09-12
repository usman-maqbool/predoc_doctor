
from django.urls import path
from .views import ForgetSuccesFullMessagePAgeView, LogInPageView, LogOutPageView,SignUpPageView , ForgetPasswordPageView,ResetForgotPasswordPAgeView


# app_name = 'account'
urlpatterns = [
    
    path('signup/',SignUpPageView.as_view(),name='sign_up'),
    path('login/',LogInPageView.as_view(),name='login'),
    path('logout/',LogOutPageView.as_view(), name='logout'),
    
    path('forget/password/',ForgetPasswordPageView.as_view(),name='forget_password'),
    path('reset/forget/password/',ResetForgotPasswordPAgeView.as_view(),name='reset_forget_password'),
    path('forgot/successfull/message/',ForgetSuccesFullMessagePAgeView.as_view(),name='forgot_successfull_message'),
    # path('register/',register_view,name='register'),

    
]


