from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculate():
    x = 1
    y = 2
    return x

def hey(request):
    x = calculate()
    return render(request,'hey.html',{
        'name': 'anything'
    })