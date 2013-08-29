from django.conf.urls import patterns, url
from projects.views import ProjectListView

urlpatterns = patterns('projects.views',
                       url(r'^$', ProjectListView.as_view(), name="projects_index"),
                       #url(r'^tag/(?P<pk>\d+)/$'),
                       #url(r'^lang/(?P<pk>\d+)/')
                       )