from django.conf.urls import url
from Overlay import views

urlpatterns = [
    url(r'^$',
        views.main,
        name='main'),

    url(r'^test/$',
        views.checks,
        name='checks'),

    url(r'^results/$',
        views.results,
        name='results'),

    url(r'^custom/$',
        views.custom,
        name='custom'),

    url(r'^RSS/$',
        views.RSS,
        name='RSS'),
    
    url(r'^custom/(?P<cnty>[^0-9]+)/$',
        views.year,
        name='years'),
    
    url(r'^custom/(?P<cnty>[^0-9]+)/(?P<yr>[0-9]{4})/$',
        views.att,
        name='attribute'),

    url(r'^custom/(?P<cnty>[^0-9]+)/(?P<yr>[0-9]{4})/(?P<fld>[^0-9]+)/$',
        views.table,
        name='table'),
]
