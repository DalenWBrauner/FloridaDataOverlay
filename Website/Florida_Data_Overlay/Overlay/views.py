from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from Overlay.models import Births
from Overlay.models import Upload
from Overlay.forms import UploadForm
from Overlay.forms import ChoosyForm
import random
import datetime
import time



def main(request):
    template=loader.get_template('main.html')
    context=RequestContext(request)
    
    return HttpResponse(template.render(context))

def test(request):
    template=loader.get_template('test.html')
    context=RequestContext(request)
    
    return HttpResponse(template.render(context))

def checks(request):
    my_list_c = Births.objects.values('county').distinct()
    len_c = len(my_list_c)
    my_list_y = Births.objects.order_by('-year').values('year').distinct()

    obj = Births.objects.get(id=1)
    names = obj.get_names()
    fields = obj.get_fields()
    d = []

    for i in range(0, len(names)):
        if ((names[i] != 'County') and
            (names[i] != 'Year') and
            (names[i] != 'Id') and
            (names[i] != 'Source') and
            (names[i] != 'Births')):

            d.append([names[i], fields[i]])
    
    template=loader.get_template('checks.html')
    context = RequestContext(request, {'c_list': my_list_c,
                                       'len_c': len_c,
                                       'y_list': my_list_y,
                                       'names': names,
                                       'fields': fields,
                                       'dict': d})
    
    return HttpResponse(template.render(context))


def results(request):
    template=loader.get_template('results.html')
    context=RequestContext(request)
    
    return HttpResponse(template.render(context))
    

def custom(request):
    my_list = Births.objects.values('county').distinct()
    
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
    fld_opts = Births.objects.values_list(fld).distinct()
    opts = []
    
    #<DALEN>
    if fld == 'mothersEdu':
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

def upload(request):
    # When the user has attempted to upload:
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            newUp = Upload(upfile = request.FILES['upfile'])
            newUp.save()

            # Redirect to the document list after POST
#            return HttpResponseRedirect(reverse('FloridaDataOverlay.Overlay.views.list'))
            return HttpResponseRedirect(reverse('Overlay.views.upload'))
    else:
        form = UploadForm() # A empty, unbound form

    # Load documents for the list page
    uploads = Upload.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'upload.html',
        {'uploads': uploads, 'form': form},
        context_instance=RequestContext(request)
    )


def graph(request, cnty, yr, fld):
    my_list = Births.objects.all().filter(county__exact = cnty)
    my_list = my_list.filter(year__exact = yr)

    raw_data = []
    data = []
    fld_opts = Births.objects.values_list(fld).distinct()
    opts = []
    
    #<DALEN>
    if fld == 'mothersEdu':
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
####################################################################

    xdata = opts
    ydata =  data

    chartdata = {
        'x': xdata, 'name1': '', 'y1': ydata, 
    }
    charttype = "discreteBarChart"
    chartcontainer = 'discretebarchart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': True,
        },
    }

    return render_to_response('graph.html', data)   

def demo_linewithfocuschart(request):
    """
    linewithfocuschart page
    """
    nb_element = 100
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)

    xdata = range(nb_element)
    xdata = map(lambda x: start_time + x * 1000000000, xdata)
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata)
    ydata3 = map(lambda x: x * 3, ydata)
    ydata4 = map(lambda x: x * 4, ydata)

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"},
                   "date_format": tooltip_date}
    chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie,
        'name3': 'series 3', 'y3': ydata3, 'extra3': extra_serie,
        'name4': 'series 4', 'y4': ydata4, 'extra4': extra_serie
    }
    charttype = "lineWithFocusChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata
    }
    return render_to_response('linewithfocuschart.html', data)
Template example:

{% load static %}
<link media="all" href="{% static 'nvd3/src/nv.d3.css' %}" type="text/css" rel="stylesheet" />
<script type="text/javascript" src='{% static 'd3/d3.min.js' %}'></script>
<script type="text/javascript" src='{% static 'nvd3/nv.d3.min.js' %}'></script>

{% load nvd3_tags %}
<head>
    {% load_chart charttype chartdata "linewithfocuschart_container" True "%d %b %Y %H" %}
</head>
<body>
    {% include_container "linewithfocuschart_container" 400 '100%' %}
</body>                               
    
