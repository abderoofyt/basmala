from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "Shamika":{'name':'Shamika', 'age': 25},
        "Junaid":{'name':'Junaid', 'age':28}
    }
    return render(request, "home.html", context)