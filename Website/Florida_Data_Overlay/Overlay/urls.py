from django.conf.urls import url
from Overlay import views

urlpatterns = [
    url(r'^$',
        views.main,
        name='main'),

    url(r'^checks/$',
        views.checks,
        name='checks'),

    url(r'^results/$',
        views.results,
        name='results'),

    url(r'^upload/$',
        views.upload,
        name='upload')
]
