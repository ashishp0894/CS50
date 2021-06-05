from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Hello/index.html")

def Brian(request):
    return HttpResponse("Hello Brian")

def David(request):
    return HttpResponse("Hello David")

def Greet(request,name):
    return render(request,"Hello/Greet.html", {
        "name":name
    }
    )