from django.http import HttpResponse

def index(request):
    return HttpResponse("Ola mundo! Esse é polls index.")