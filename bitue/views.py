from django.shortcuts import render
from django.http import HttpResponse

from bitue.forms import contact_form

def index(request):
    
    
    print(request.POST)
    if request.POST :
        form = contact_form(request.POST, request.FILES)
        dic ={"name": "My Name is bitue " , 'email': request.POST.get('user_name'), 'pass': request.POST.get('pass') , 'form': form}
        if form.is_valid():
            
            file = form.cleaned_data['profile']
            with open ('./bitue/upload/' + file.name , "wb+") as ds :
                for chunk in file.chunks() :
                    ds.write(chunk)
            return render (request, 'bitue/index.html', context=dic)
        else :
            form = contact_form()
        
    return render (request, 'bitue/index.html', context=dic)
    


def contact(request):
    return HttpResponse("<h1>This is contact page</h1> <a href='/bitue/' > Home</a> <a href='/bitue/about/' > About</a>")

def about(request):
    return HttpResponse("<h1>this is about page </h1><a href='/bitue/contact/' > Contact</a> <a href='/bitue/' >Home</a>")



