from django.template import loader
from django.http import HttpResponse

# Create your views here.

def getStartPg(request):
    return HttpResponse((loader.get_template('index.html')).render({}, request))
