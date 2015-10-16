from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from ucpd.views import *

urlpatterns = [
    url(r'^$', Main.as_view(), name='bins'),

    url(r'^api/bins.json/$', BinsJSON.as_view(), name='bins-json'),
    url(r'^api/hours.json/$', HoursJSON.as_view(), name='hours-json'),
    url(r'^months.csv/$', months, name='months'),
    url(r'^hours.csv/$', hours, name='hours'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)