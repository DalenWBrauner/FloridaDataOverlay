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

def RSS(request):
    template=loader.get_template('RSS.html')
    context=RequestContext(request)
    
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
        #add if statements HERE instead of template
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

    raw_data = []
    data = []
    #fld_opts2 = Births.objects.values(fld).distinct()
    fld_opts = Births.objects.values_list(fld).distinct()
    opts = []


    # <DALEN CODE>
    if   fld == 'mothersEdu':
        # This is actually identical to Becca's for loop,
        # just scrunched into less lines.
        for i in fld_opts:
            opts.append( str(i)[3:-3] )
            
    elif fld == 'isRepeat':
        for i in fld_opts:
            opts.append(i[0])
            
    elif fld == 'mothersAge':
        for i in fld_opts:
            opts.append(i[0])
        
    else:
        print "Errr.....",fld
    # </DALEN CODE>

    for i in opts:
        trans = []
        cond = 0
        loop_list = my_list.filter(**{fld + '__exact' : i})

        for j in loop_list:
            cond = 1
            trans.append(j.births)

        if cond == 1:
            raw_data.append(trans)

        else:
            raw_data.append([0])

    for i in raw_data:
        sum_births = 0
        
        for j in i:
            sum_births += j
            
        data.append(sum_births)

    da_list = []

    for i in range(0, len(opts)):
        t = []
        #eventually this will be dynamic: # of years + 1

        t.append(opts[i])
        t.append(data[i])
            
        da_list.append(t)

    rng = []
    
    if da_list[0]:
        for i in range(0, len(da_list[0])):
            rng.append(i)
    
    template = loader.get_template('table.html')
    context = RequestContext(request, {'county': cnty,
                                       'year': yr,
                                       'field': fld,
                                       'options': opts,
                                       'data': data,
                                       'range': rng,
                                       'da_list': da_list})
    
    return HttpResponse(template.render(context))
