from django.conf.urls import patterns, url

from graphos import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
