from django.shortcuts import render
from django import forms
from django.http import JsonResponse, HttpResponse
import json
from djangomix.templatetags.mix import mix
import time

class LoginForm(forms.Form):
    username = forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)
    
    class Media:
        js = ( mix('dist/form.js'),  )


    @property
    def params(self):
        d = {}
        for name, field in self.fields.items():
            d[name] = self[name].value() or ''
        return d



def home(request):
    f = LoginForm()
    if request.method == "POST":
        f = LoginForm(json.loads(request.body))
        if f.is_valid():
            pass
        else:
            time.sleep(2)
            json_response = f.errors.as_json()
            return HttpResponse(f.errors.as_json(), status=422)

    context = {
        'form': f
    }
    return render(request,"base.html", context)

