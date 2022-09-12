

# from django .core.mail import send_mail
# from django.conf import settings

# import uuid


# def send_foregt_password_email (email,token):
#     token
#     subject = 'Your Forget Password Link'
#     message = f'Hi, click on the link to reset your password http://127.0.0.1:8000/account/reset/forget/password/{token}/'
#     email_from = settings.EMAIL_HOST_USER
#     recepint_list = [email]
#     send_mail(subject,message,email_from,recepint_list)
#     return True


from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class AppTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return (text_type(user.is_active) + text_type(user.pk) + text_type(timestamp))


