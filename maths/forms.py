from django import forms

class MathsForm(forms.Form):
    a = forms.IntegerField(required=False)
    b = forms.IntegerField(required=False)
    x = forms.CharField(required=False)

class MathForm(forms.Form):
    c = forms.CharField(required=False)
