
from django.urls import path
from .views import LogInPageView, LogOutPageView,SignUpPageView


# app_name = 'account'
urlpatterns = [
    
    path('login/',LogInPageView.as_view(),name='login'),
    path('logout/',LogOutPageView.as_view(), name='logout'),
    
    path('signup/',SignUpPageView.as_view(),name='sign_up'),
    # path('register/',register_view,name='register'),

    
]


