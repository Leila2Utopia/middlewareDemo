from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    print('views')
    return HttpResponse('views')