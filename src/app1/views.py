from django.shortcuts import render
#from django.http import HttpResponse
from .models import Resume

#def index(request):
#    return HttpResponse(" Hello, Abel.  It's polls index. ;) ")

def index(request):
    resume_list = Resume.objects.all()
    ctx = {
        "resume_list" : resume_list
    }
    return render(request, "index.html", ctx )
