from django.shortcuts import render
from traitlets import Int
from .forms import MathsForm, MathForm

# Create your views here.
def maths_view(request):
    sum = 0
    sums = 0
    # form = MathsForm(request.POST or None) #doesn't display it online
    if request.method == "POST":
        form = MathsForm(request.POST or None)
        forms = MathForm(request.POST or None)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            x = form.cleaned_data['x']
            if (x =='+'):
                sum = a + b
            elif (x == '-'):
                sum = a - b
            elif (x == '*' or x.lower() == 'x'):
                sum = a * b
            elif (x == '/'):
                sum = a / b
            elif (x == '%'):
                sum = a % b

        if forms.is_valid():
            c = forms.cleaned_data['c']
            if (len(c)>0):
                sums = eval(c)
        return render(request, 'maths.html', {'form':form, 'forms':forms, 'sum':sum, 'sums':sums})

    else:
        form = MathsForm()
        forms = MathForm()
    
    return render(request, 'maths.html', {'form':form, 'forms':forms, 'sum':sum, 'sums':sums})
