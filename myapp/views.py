
from django.http import HttpResponse, JsonResponse
from .models import Project , Task
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, "about.html")

def hello(request, username):
    print(username)
    
    return HttpResponse("<h1>HOLAAAAAAAAA %s</h1>" % username)


def projects(request):
   # projects = list(Project.objects.values())
    projects = list(Project.objects.all())
    return render(request, 'projects.html',{
        'projects': projects
    })
    
def task(request):
    #task =list(Task.objects.values())
    return render(request, 'task.html')
    