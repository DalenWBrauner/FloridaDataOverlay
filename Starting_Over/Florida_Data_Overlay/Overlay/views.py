from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from Overlay.models import Births

def main(request):
    template=loader.get_template('main.html')
    context=RequestContext(request)
    
    return HttpResponse(template.render(context))

def custom(request):
    my_list=Births.objects.values('county').distinct()
    
    template=loader.get_template('custom.html')
    context=RequestContext(request, {'my_list': my_list})
    
    return HttpResponse(template.render(context))

def year(request, cnty):
    my_list = Births.objects.all().filter(county__exact = cnty)
    my_list = my_list.order_by('-year').values('year').distinct()
    
    template = loader.get_template('years.html')
    context = RequestContext(request, {'county': cnty,
                                       'my_list': my_list})
    
    return HttpResponse(template.render(context))

def att(request, cnty, yr):
    obj = Births.objects.get(id=1)
    names = obj.get_names()
    fields = obj.get_fields()
    d = []

    for i in range(0, len(names)):
        d.append([names[i], fields[i]])
    
    template = loader.get_template('attribute.html')
    context = RequestContext(request, {'county': cnty,
                                       'year': yr,
                                       'names': names,
                                       'fields': fields,
                                       'dict': d})
    
    return HttpResponse(template.render(context))

def table(request, cnty, yr, fld):
    my_list = Births.objects.all().filter(county__exact = cnty)
    my_list = my_list.filter(year__exact = yr)
    data = my_list.values(fld)
    
    template = loader.get_template('table.html')
    context = RequestContext(request, {'county': cnty,
                                       'year': yr,
                                       'field': fld,
                                       'data': data,
                                       'my_list': my_list})
    
    return HttpResponse(template.render(context))
