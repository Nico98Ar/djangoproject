
from django.http import HttpResponse, JsonResponse
from .models import Project , Task
# Create your views here.

def index(request):
    return HttpResponse("HOLA MUNDOOOOO")


def hello(request, username):
    print(username)
    return HttpResponse("<h1>HOLAAAAAAAAA %s</h1>" % username)

def about(request):
    return HttpResponse("NICOOOOOOOOOOOOO")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)
    
def task(request):
    task =list(Task.objects.values())
    return JsonResponse(task, safe=False)
    