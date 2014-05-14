from django.core.urlresolvers import reverse
from django.forms.models import modelformset_factory
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from Overlay.forms import BirthForm
from Overlay.forms import UploadForm
from Overlay.models import Births
from Overlay.models import Upload



def main(request):
    template=loader.get_template('main.html')
    context=RequestContext(request)
    
    return HttpResponse(template.render(context))

def test(request):
    '''
    if request.method == 'POST':
        form = BirthForm(request.POST)

        if form.is_valid():
            #SOMETHING GRAPHY TO BE DONE HERE
            return HttpResponseRedirect(reverse('test')) #this redirects it to the same page, which is cool

    else:
        form = BirthForm()

    return render(request, 'test.html', {'form': form})
'''

    form = BirthForm()

    return render(request, 'test.html', {'form': form})
    
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
    message = "message: \n"
    
    if 'counties' in request.GET:
        message = message + 'counties : %r \n' % request.GET.getlist('counties')
    
    else:
        message = message + 'no counties'
        
    if 'years' in request.GET:
        message = message + 'years : %r \n' % request.GET.getlist('years')
    
    else:
        message = message + 'no years'
        
    if 'attributes' in request.GET:
        message = message + 'attributes : %r \n' % request.GET.getlist('attributes')
    
    else:
        message = message + 'no attributes'

    return render(request, 'results.html', {'message': message})
    

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

    #AFTER THIS POINT USE OPTS AND DATA
    
    template = loader.get_template('graph.html')
    #add stuff down below if you need to pass it to the template
    #'template name': variable name
    context = RequestContext(request, {'county': cnty,
                                       'year': yr,
                                       'field': fld,
                                       'options': opts,
                                       'data': data})
    
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
