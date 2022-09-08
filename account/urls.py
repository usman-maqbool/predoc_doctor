
from django.urls import path,include
from .views import LogInPageView,Lsnding



# app_name = 'account'
urlpatterns = [
    
    path('login/',LogInPageView.as_view(),name='login'),
    
]


