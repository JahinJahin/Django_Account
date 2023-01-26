from django import forms
from medicine.models import medicine
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MedicineForm(forms.ModelForm):
    class Meta:
        model = medicine
        fields = "__all__"

class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
