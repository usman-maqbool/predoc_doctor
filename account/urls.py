
from django.contrib.auth.views import (PasswordResetCompleteView,
                                       PasswordResetConfirmView)
from django.urls import path

from .views import (LogInView, LogOutView, ResetPasswordDoneView, SignUpView,
                    VerificationEmailView, VerificationView,
                    password_reset_request)

# app_name = 'account'
urlpatterns =  [
    #signup
    path('signup/', SignUpView.as_view(),name='sign_up'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),
    path('verification', VerificationEmailView.as_view(),name='verify'),
    #login
    path('login/', LogInView.as_view(),name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    #forget password
    path('forget/password', password_reset_request, name ='forget_password'),
    path('reset/password/done', ResetPasswordDoneView.as_view(), name ='reset_password_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name ='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='accounts/reset_password_complete.html'),name='password_reset_complete'),
]

