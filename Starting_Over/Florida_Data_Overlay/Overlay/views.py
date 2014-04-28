from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from Overlay.models import Births

#def basic(request):
#    my_list=list(Births.objects.all())
#    render basic_temp.html, my_list

def basic(request):
#    list = Births.objects.order_by('-County')[:5]
#    my_list = (Births.objects.all().order_by('-county'))[:5]
    my_list=Births.objects.values('county').distinct()
    template=loader.get_template('base.html')
    context=RequestContext(request, {'my_list': my_list})
    
    return HttpResponse(template.render(context))

def year(request, cnty):
    my_list = Births.objects.all().filter(county__exact = cnty).order_by('-year').values('year').distinct()
    template = loader.get_template('years.html')
    context = RequestContext(request, {'my_list': my_list})
    
    return HttpResponse(template.render(context))

def att(request, county, year):
    html='<html><body>derp</body></html>'
    return HttpResponse(html)
