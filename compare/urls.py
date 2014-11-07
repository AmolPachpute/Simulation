from django.conf.urls import patterns, include, url
from compare.views import Compare
urlpatterns = patterns('',
    # Examples:
    url(r'^$', Compare.as_view(), name='compare'),

)