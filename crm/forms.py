from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class Login(UserCreationForm):
    class Meta:
        model=User
        fields=["id","username","password","email",]





c
