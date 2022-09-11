from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hey(request):
    # things we can do
    # pull data from db
    # transform data
    # send email and so on
    return HttpResponse("HELLO BITCHES")

def nothing(request):
    return HttpResponse("Nothing to see here")