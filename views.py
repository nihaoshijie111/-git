from django.http import HttpResponse


def index(request):
    return HttpResponse('hh'
            

def login(request):
    return redirect('/index')
