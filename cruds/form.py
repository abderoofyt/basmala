from django import forms
from .models import GeeksModel, Students

class My_Form(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"

class GeeksForm(forms.ModelForm):
    class Meta:
        model = GeeksModel
        fields = ["title", "description",]