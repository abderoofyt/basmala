# Create your views here.
from gc import get_objects
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .form import My_Form
from .models import Student

def index(request):
    stu = My_Form()
    return render(request,"input.html", {'form':stu})

def post(request):
    form = My_Form()
    if request.method == "POST":
        form = My_Form(request.POST)
    if form.is_valid():
        try:
            return HttpResponse("<h1>Welcome!</h1>")
        except:
            pass
    else:
        form = My_Form()
    return render(request,"input.html", {'form':form})
    