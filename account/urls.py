
from django.urls import path
from .views import LogInPageView, LogOutPageView, VerificationEmailPageView, VerificationView, password_reset_request,ResetPasswordConfirmPageView, ResetPasswordDonePageView,SignUpView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views  import PasswordResetView , PasswordResetConfirmView , PasswordResetCompleteView,PasswordResetDoneView

# app_name = 'account'
urlpatterns =  [
    #SignUp
    path('signup/',SignUpView.as_view(),name='sign_up'),
    path('activate/<uidb64>/<token>',VerificationView.as_view(), name='activate'),
    path('verification',VerificationEmailPageView.as_view(),name='verify'),
    # Log In
    path('login/',LogInPageView.as_view(),name='login'),
    path('logout/',LogOutPageView.as_view(), name='logout'),
    #Forget Password
    path('forget/password',password_reset_request, name ='forget_password'),
    path('reset/password/done', ResetPasswordDonePageView.as_view(), name ='reset_password_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name ='password_reset_confirm'),
    path('reset/done/',PasswordResetCompleteView.as_view(template_name='accounts/reset_password_complete.html'),name='password_reset_complete'),
]



# urlpatterns = [
#     path('signup/',SignUpPageView.as_view(),name='sign_up'),
#     path('login/',LogInPageView.as_view(),name='login'),
#     path('logout/',LogOutPageView.as_view(), name='logout'),
#     path(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='forget_password'),
#     path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
# ]


