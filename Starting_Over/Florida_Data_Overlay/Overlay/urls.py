from django.conf.urls import url
from Overlay import views

urlpatterns = [
    url(r'^$', views.basic, name='basic'),
    url(r'^(?P<county>[^0-9]+)/$', views.year, name='years'),
]
