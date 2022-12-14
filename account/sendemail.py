import random
import string

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

# BASE_LINK_FOR_EMAIL ="http://127.0.0.1:8000"
BASE_LINK_FOR_EMAIL ="https://predoc.com.au"

class AppTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return (text_type(user.is_active) + text_type(user.pk) + text_type(timestamp))

def get_random_string():
    return ''.join(random.choices(string.ascii_uppercase +string.digits, k=30))

account_activation_token = AppTokenGenerator()

