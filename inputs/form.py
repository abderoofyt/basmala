from django import forms
from .models import Student

class My_Form(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
