from django.shortcuts import render
from django.http import HttpResponse

def basic(request):
    #Births.objects.all()
    #html = "<html><body>INSERT THING HERE</body></html>"

    my_list=list(Births.objects.all())
    render basic_temp.html, my_list
