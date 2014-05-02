from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^overlay/', include('Overlay.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', RedirectView.as_view(url='/overlay/upload/')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
