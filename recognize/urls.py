from django.conf.urls import patterns, include, url
from recognize.views import Recognize
urlpatterns = patterns('',
    # Examples:
    url(r'^$', Recognize.as_view(), name='app1home'),

)