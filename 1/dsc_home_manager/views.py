from django.http import HttpResponse

def index(request):
    return HttpResponse("<html><head><title>Deepin Software Center Home Data</title></head><body><a href='admin'>Admin</a></body></html>")
