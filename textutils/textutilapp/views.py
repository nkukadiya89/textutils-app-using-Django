from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("<h1>About Page</h1>")

def removepunc(request):
    return HttpResponse("removepunc") 

def capfirst(request):
    return HttpResponse("capfirst")

def newlineremove(request):
    return HttpResponse("newlineremove")

def spaceremover(request):
    return HttpResponse("spaceremover")

def charcount(request):
    return HttpResponse("charcount")

def analyzer(request):
    djtext = request.GET.get('djtext','default')
    action = request.GET.get('option1')
    analyzed_text = ""
    if action == "on":
        punc = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for tex in djtext:
            print(tex)
            if tex not in punc: 
                analyzed_text = analyzed_text + tex
    
        return render(request,'analyzer.html',{'analyzed_text':analyzed_text, 'action':action})
    else:
        return HttpResponse("error")    