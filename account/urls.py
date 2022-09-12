
from django.urls import path
from .views import LogInPageView, LogOutPageView, password_reset_request,ResetPasswordConfirmPageView, ResetPasswordDonePageView,SignUpPageView


# app_name = 'account'
urlpatterns = [
    
    path('signup/',SignUpPageView.as_view(),name='sign_up'),
    path('login/',LogInPageView.as_view(),name='login'),
    path('logout/',LogOutPageView.as_view(), name='logout'),
    path('forget/password',password_reset_request, name ='forget_password'),
    path('reset/password/done', ResetPasswordDonePageView.as_view(), name ='reset_password_done'),
    path('reset/<uidb64>/<token>/', ResetPasswordConfirmPageView.as_view(), name ='password_reset_confirm'),
    
    
    

    
]


