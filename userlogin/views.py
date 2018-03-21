from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from userreg.models import UserDetails as ud
from django.db.models import Q

# Create your views here.

def getLoginPg(request):
    return HttpResponse((loader.get_template('userlogin/login.html')).render({}, request))

def verify(request):
    try :
        if (request.method=='POST'):
                email=request.POST.get('eml','empty')
                passw=request.POST.get('pss','empty')
                if ud.objects.get(Q(eml=email)&Q(pss=passw)):
                    return HttpResponse((loader.get_template('dashboard.html')).render({'name':(ud.objects.get(Q(eml=email)&Q(pss=passw))).usr_name}, request))
                else:
                    return render(request, 'userlogin/login.html',{'data': "Login Unsuccessful!!", 'col_code': '0'})
        else:
            return render(request, 'userlogin/login.html',{'data': "Login Unsuccessful!!", 'col_code': '0'})
    except :
        return render(request, 'userlogin/login.html',{'data': "Login Unsuccessful!!", 'col_code': '0'})
