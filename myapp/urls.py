# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from . import views
from . import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Hello, world!
    url(r'^$', views.index, name='index'),
    
]