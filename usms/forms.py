from django.forms import ModelForm
from .models import *


class UserForm(ModelForm):
    class Meta:
        model = InnstalUser
        # fields = '__all__'
        exclude = ['is_superuser', 'is_staff', 'is_active', 'is_active_subscription', 'user_type', 'email', 'password']
