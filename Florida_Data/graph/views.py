from django.http import HttpResponse
#from graphos.renderers import gchart

def index(request):
    return HttpResponse("Hello, world. Put a graph here.")


#chart = gchart.LineChart(utils.data)
