from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .datahandling.FileOps import getWordList as gwl,getFinalFilterdText as gfft
from .datahandling.WebCrawl import fromWeb as fw,fromWebAgain as fwa
from django.conf import settings

def getUplPage(request):
    return render(request, 'docchecker/doccheck.html', {})

def getTest(request):
    return render(request, 'text.html', {})

def getResp(request):
    if request.method == 'POST':
        if request.FILES['myfile']:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                lstofres=fw(gfft(gwl(settings.MEDIA_ROOT+'/'+filename)))
                #return render(request, 'docchecker/doccheck.html', {'file_url': uploaded_file_url,'col_code':'1'})
                return render(request, 'docchecker/results_mod.html', {'results':lstofres})
        else:
            return render(request, 'dashboard.html', {'name':request.POST['nm']})

def getAct(request):
    text=request.POST['txt']
    lstofres = fwa(text)
    return render(request, 'docchecker/results_mod.html', {'results': lstofres})