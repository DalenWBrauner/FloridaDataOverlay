from django.conf.urls import url
from Overlay import views

urlpatterns = [
    url(r'^$',
        views.basic,
        name='basic'),
    
    url(r'^(?P<cnty>[^0-9]+)/$',
        views.year,
        name='years'),
    
    url(r'^(?P<cnty>[^0-9]+)/(?P<yr>[0-9]{4})/$',
        views.att,
        name='attribute'),

    url(r'^(?P<cnty>[^0-9]+)/(?P<yr>[0-9]{4})/(?P<fld>[^0-9]+)/$',
        views.table,
        name='table'),
]
