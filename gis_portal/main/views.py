from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.serializers import serialize
from . import models
# Create your views here.
# def school(request):
#     schoolData=serialize('geojson', School.objects.all())
#     return HttpResponse(schoolData, content_type='geojson')

def ahmadnagar(request):
    ahmadnagarData=serialize('geojson', models.Ahmadnagar.objects.all())
    return HttpResponse(ahmadnagarData, content_type='geojson')

def akola(request):
    akolaData=serialize('geojson', models.Akola.objects.all())
    return HttpResponse(akolaData, content_type='geojson')

def amravati(request):
    amravatiData=serialize('geojson', models.Amravati.objects.all())
    return HttpResponse(amravatiData, content_type='geojson')

def aurangabad(request):
    aurangabadData=serialize('geojson', models.Aurangabad.objects.all())
    return HttpResponse(aurangabadData, content_type='geojson')

def beed(request):
    beedData=serialize('geojson', models.Beed.objects.all())
    return HttpResponse(beedData, content_type='geojson')

def bhandara(request):
    bhandaraData=serialize('geojson', models.Bhandara.objects.all())
    return HttpResponse(bhandaraData, content_type='geojson')

def buldana(request):
    buldanaData=serialize('geojson', models.Buldhana.objects.all())
    return HttpResponse(buldanaData, content_type='geojson')

def chandrapur(request):
    chandrapurData=serialize('geojson', models.Chandrapur.objects.all())
    return HttpResponse(chandrapurData, content_type='geojson')

def dhule(request):
    dhuleData=serialize('geojson', models.Dhule.objects.all())
    return HttpResponse(dhuleData, content_type='geojson')

def gadchiroli(request):
    gadchiroliData=serialize('geojson', models.Gadchiroli.objects.all())
    return HttpResponse(gadchiroliData, content_type='geojson')

def hingoli(request):
    hingoliData=serialize('geojson', models.Hingoli.objects.all())
    return HttpResponse(hingoliData, content_type='geojson')

def jalgaon(request):
    jalgaonData=serialize('geojson', models.Jalgaon.objects.all())
    return HttpResponse(jalgaonData, content_type='geojson')

def jalna(request):
    jalnaData=serialize('geojson', models.Jalna.objects.all())
    return HttpResponse(jalnaData, content_type='geojson')

def kolhapur(request):
    kolhapurData=serialize('geojson', models.Kolhapur.objects.all())
    return HttpResponse(kolhapurData, content_type='geojson')

def latur(request):
    laturData=serialize('geojson', models.Latur.objects.all())
    return HttpResponse(laturData, content_type='geojson')

def mumbai(request):
    mumbaiData=serialize('geojson', models.Mumbaifull.objects.all())
    return HttpResponse(mumbaiData, content_type='geojson')

def nagpur(request):
    nagpurData=serialize('geojson', models.Nagpur.objects.all())
    return HttpResponse(nagpurData, content_type='geojson')

def nanded(request):
    nandedData=serialize('geojson', models.Nanded.objects.all())
    return HttpResponse(nandedData, content_type='geojson')

def nandurbar(request):
    nandurbarData=serialize('geojson', models.Nandurbar.objects.all())
    return HttpResponse(nandurbarData, content_type='geojson')

def nashik(request):
    nashikData=serialize('geojson', models.Nashik.objects.all())
    return HttpResponse(nashikData, content_type='geojson')

def osmanabad(request):
    osmanabadData=serialize('geojson', models.Osmanabad.objects.all())
    return HttpResponse(osmanabadData, content_type='geojson')

def parbhani(request):
    parbhaniData=serialize('geojson', models.Parbhani.objects.all())
    return HttpResponse(parbhaniData, content_type='geojson')

def pune(request):
    puneData=serialize('geojson', models.Pune.objects.all())
    return HttpResponse(puneData, content_type='geojson')

def raigad(request):
    raigadData=serialize('geojson', models.Raigad.objects.all())
    return HttpResponse(raigadData, content_type='geojson')

def ratnagiri(request):
    ratnagiriData=serialize('geojson', models.Ratnagiri.objects.all())
    return HttpResponse(ratnagiriData, content_type='geojson')

def sangli(request):
    sangliData=serialize('geojson', models.Sangli.objects.all())
    return HttpResponse(sangliData, content_type='geojson')

def satara(request):
    sataraData=serialize('geojson', models.Satara.objects.all())
    return HttpResponse(sataraData, content_type='geojson')

def sindhudurg(request):
    sindhudurgData=serialize('geojson', models.Sindhudurg.objects.all())
    return HttpResponse(sindhudurgData, content_type='geojson')

def solapur(request):
    solapurData=serialize('geojson', models.Solapur.objects.all())
    return HttpResponse(solapurData, content_type='geojson')

def thane(request):
    thaneData=serialize('geojson', models.Thane.objects.all())
    return HttpResponse(thaneData, content_type='geojson')

def wardha(request):
    wardhaData=serialize('geojson', models.Wardha.objects.all())
    return HttpResponse(wardhaData, content_type='geojson')

def washim(request):
    washimData=serialize('geojson', models.Washim.objects.all())
    return HttpResponse(washimData, content_type='geojson')

def yavatmal(request):
    yavatmalData=serialize('geojson', models.Yavatmal.objects.all())
    return HttpResponse(yavatmalData, content_type='geojson')


def home(response):
    return render(response, "main/home.html",{"name":"Home"})

def map(response):
    return render(response, "main/map.html",{"name":"Map"})
