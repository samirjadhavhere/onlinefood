from django.db import models

class register(models.Model):
    username=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=45,null=True)

    def __str__(s):
        return str(s.id)+" "+s.username
    class Meta:
        db_table="reg"

from django import forms
from django.contrib.auth.models import User

class Loginform(forms.Form):
    email=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)

class EditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password"]