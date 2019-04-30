from django.shortcuts import render
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)



def home(request):
    f = LoginForm()
    if request.method == "POST":
        f = LoginForm(request.POST)
        if f.is_valid():
            pass

    context = {
        'form':f
    }
    return render(request,"base.html", context)

