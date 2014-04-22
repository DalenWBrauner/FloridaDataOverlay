from django.conf.urls import url
from Overlay import views

urlpatterns = [
    url(r'^$', views.basic, name='basic')
]
