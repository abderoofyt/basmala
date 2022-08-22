# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def strings(request):
    print('Hello, World!')
    console_log = "<script>console.log('Hello world!')</script>"
    return HttpResponse(console_log)

def hello(request):
    return HttpResponse("Hello, World!")

def bismala(request):
    bismala = {
        'arabic':"<p>بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ</p>",
        'trans':"<p> bismillāhi r-raḥmāni r-raḥīm </p>",
        'english':"<p>In the name of Allah, the Most Gracious, the most Merciful</p>"
    }
    return HttpResponse(bismala)

def bismala_variable(request):
    context = "<h3>(In the name of Allah)</h3>"
    return HttpResponse("<h1>Bismillah </h1>"+"<h2>بسم الله <h2>"+context)
    

def home(request):
    template = loader.get_template('home.html')
    bismala = {
        'arabic':"<p>بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ</p>",
        'trans':"<p> bismillāhi r-raḥmāni r-raḥīm </p>",
        'english':"<p>In the name of Allah, the Most Gracious, the most Merciful</p>"
    }
    return HttpResponse(template.render(bismala))

def bismala_list(request):
    template = loader.get_template('list.html')
    bismala = {
        'arabic':"بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ",
        'trans':"bismillāhi r-raḥmāni r-raḥīm ",
        'english':"In the name of Allah, the Most Gracious, the most Merciful."
    }
    return HttpResponse(template.render(bismala))
    
def context(request):
    context = {
        "Shamika":{'name':'Shamika', 'age': 25},
        "Junaid":{'name':'Junaid', 'age':28}
    }
    return render(request, "index.html", context)