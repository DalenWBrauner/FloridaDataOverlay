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
    my_list=Births.objects.all()
    template=loader.get_template('base.html')
    context=RequestContext(request, {'my_list': my_list})
    
    return HttpResponse(template.render(context))
