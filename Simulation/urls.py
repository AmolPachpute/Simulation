from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from recognize.views import Recognize


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'pearson.views.home', name='home'),
    url(r'^recognize/$', include('recognize.urls')),
    url(r'^analyze/', include('analyze.urls')),
    url(r'^compare/', include('compare.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
