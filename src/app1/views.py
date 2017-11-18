from django.shortcuts import render
#from django.http import HttpResponse

#def index(request):
#    return HttpResponse(" Hello, Abel.  It's polls index. ;) ")

def index(request):
    name = "abel"
    return render(request, "index.html", { "name" : name })
