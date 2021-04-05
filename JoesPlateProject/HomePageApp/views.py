from django.shortcuts import render
from restorantApp.models import *

def LandingPage(request):
    restmdl = restorantModel.objects.all().order_by('-rest_reg_date')
    context = {
        'restmdl': restmdl,
    }
    return render(request, 'HomePage/LandingPage.html', context)

def RestorentDetailsFun(request, restname):
    restmdl = restorantModel.objects.get(rest_url=restname)
    restmenu = restMenuModel.objects.filter(restorant=restmdl)
    context = {
        'restmdl': restmdl,
    }
    return render(request, 'HomePage/RestorentDetails.html', context)
