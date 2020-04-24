from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
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
    djtext = request.POST.get('djtext','default')
    action = request.POST.getlist('option')
    analyzed_text = ""
    if len(action)> 0 :
        for ac in action:
            if ac == "Remove punctuation":
                punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
                for tex in djtext:
                    if tex not in punc: 
                        analyzed_text = analyzed_text + tex
            elif ac == "Capitalized First":
                 analyzed_text = analyzed_text.capitalize() 
            elif ac == "New Line Remove":
                for tex in djtext:
                    if tex !='\n':
                        analyzed_text = analyzed_text + tex 
            elif ac == "Space Remover":
                space = ''' '''
                for tex in djtext:
                    if tex not in space:
                        analyzed_text = analyzed_text + tex      
            elif ac == "Char count":
                analyzed_text = len(djtext)                         
            else:
                pass     
        return render(request,'analyzer.html',{'analyzed_text':analyzed_text, 'action':action})
    
    else:
        return HttpResponse("error")    