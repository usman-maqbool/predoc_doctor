from django.shortcuts import render,redirect
from django.views import View

from django.contrib.auth import authenticate,login, logout

# Create your views here.


class LogInPageView(View):
    def get(self,request):
        context={
            "title":"LogIn"
        }
        return render(request, 'accounts/login.html' ,context)

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # Return an 'invalid login' error message.
            return redirect('login')



class Lsnding(View):
    def get(self,request):
        context={
            "title":"LogIn"
        }
        return render(request, 'accounts/login.html' ,context)



