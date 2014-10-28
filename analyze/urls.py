from django.conf.urls import patterns, include, url
from analyze.views import Analyze
urlpatterns = patterns('',
    # Examples:
    url(r'^$', Analyze.as_view(), name='app1home'),

)