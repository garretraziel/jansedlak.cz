from django.conf.urls import patterns, url

urlpatterns = patterns('projects.views',
                       url(r'^$'),
                       url(r'^tag/(?P<pk>\d+)/$'),
                       url(r'^lang/(?P<pk>\d+)/')
                       )