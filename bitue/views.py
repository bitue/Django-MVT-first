from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    dic ={"name": "My Name is bitue "}
    print(request, "req")
    return render (request, 'bitue/index.html', context=dic)
    


def contact(request):
    return HttpResponse("<h1>This is contact page</h1> <a href='/bitue/' > Home</a> <a href='/bitue/about/' > About</a>")

def about(request):
    return HttpResponse("<h1>this is about page </h1><a href='/bitue/contact/' > Contact</a> <a href='/bitue/' >Home</a>")
    
