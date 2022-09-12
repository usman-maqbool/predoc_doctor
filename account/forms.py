from ast import Try
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserModel

# Sign Up Form
class SignUpForm(UserCreationForm):
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder': 'Enter your Username', 'id':'user_name', 'class':'form-control'}),max_length=50,required=True,help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'id':'user_email', 'class':'form-control'}),max_length=50,required=True,help_text='Required.add valid email address')
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Your Password', 'id':'user_password', 'class':'form-control'}),max_length=50,required=True,help_text='Your password must contain at least 8 characters.')
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'id':'confirm_password', 'class':'form-control'}),max_length=50,required=True,help_text='Enter the same password as before, for verification.')
    class Meta:
        model = UserModel
        fields = [
            'username','email','password1','password2'
            ]

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = UserModel.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use.")


    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = UserModel.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"Email {username} is already in use.")

class LoginForm(forms.Form):
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'id':'user_email', 'class':'form-control'}),max_length=50)
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'id':'user_password', 'class':'form-control'}),max_length=50,required=True)
    class Meta:
        model = UserModel
        fields = ['email','password1']





class RecoverPasswordForm(forms.Form):
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'id':'user_email', 'class':'form-control'}),max_length=50,required=True)
    class Meta:
        models= UserModel
        fields = ['email']


# class SignUpPageForm(UserCreationForm):
#     email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'id':'user_email', 'class':'form-control'}),max_length=50,required=True,help_text='Required.add valid email address')
#     username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder': 'Enter your username', 'id':'user_name', 'class':'form-control'}),max_length=50,required=True,help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
#     password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'id':'user_password', 'class':'form-control'}),max_length=50,required=True,help_text='Your password must contain at least 8 characters.')
#     password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter confirm password', 'id':'confirm_password', 'class':'form-control'}),max_length=50,required=True,help_text='Enter the same password as before, for verification.')
#     class Meta:
#         model=UserModel
#         fields=['username','email','password1','password2']

# class LoginForm(forms.Form):
#     email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'id':'user_email', 'class':'form-control'}),max_length=50)
#     password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'id':'user_password', 'class':'form-control'}),max_length=50,required=True)
#     class Meta:
#         model = UserModel
#         fields = ['email','password']



# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(max_length=255)

#     class Meta:
#         model = UserModel
#         fields = ('email', 'username' , 'password1' , 'password2')

#     def clean_email(self):
#         email = self.cleaned_data['email'].lower()
#         try:
#             account = UserModel.objects.get(email=email)
#         except Exception as e:
#             return email
#         raise forms.ValidationError(f"Email {email} is already in use.")


#     def clean_username(self):
#         username = self.cleaned_data['username']
#         try:
#             account = UserModel.objects.get(username=username)
#         except Exception as e:
#             return username
#         raise forms.ValidationError(f"Email {username} is already in use.")

        
