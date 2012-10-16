from django.conf.urls import patterns, include, url
from courses.views import *
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ludus.views.home', name='home'),
    # url(r'^ludus/', include('ludus.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^courses/$', courses),
    url(r'^schedule/all/$', schedule),
    url(r'^schedule/c/(?P<course_id>\d+)/$', schedule),
    url(r'^schedule/d/(?P<day>\d)/$', day_schedule),
    url(r'^schedule/d/', direct_to_template, {'template': 'daylist.html'}),
    url(r'^$', direct_to_template, {'template': 'index.html'}),
)
