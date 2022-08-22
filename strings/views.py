# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def strings(request):
    print('Hello, World!')
    return HttpResponse()

def hello(request):
    return HttpResponse("Hello, World!")

def bismala(request):
    return HttpResponse("\
    <h1>Bismillah – بسم الله (In the name of Allah)</h1>\
    <p>بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ</p>\
    <p> bismillāhi r-raḥmāni r-raḥīm </p>\
    <p>In the name of Allah, the Most Gracious, the most Merciful")
    
def home(request):
    template = loader.get_template('home.html')
    students = {
        "Shamika":{'name':'Shamika', 'age': 25},
        "Junaid":{'name':'Junaid', 'age':28}
    }
    return HttpResponse(template.render(students))

def context(request):
    context = {
        "Shamika":{'name':'Shamika', 'age': 25},
        "Junaid":{'name':'Junaid', 'age':28}
    }
    return render(request, "index.html", context)