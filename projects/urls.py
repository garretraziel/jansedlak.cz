from django.conf.urls import patterns, url
from projects.views import ProjectListView, ProjectDetailView, project_fs

urlpatterns = patterns('projects.views',
                       url(r'^$', ProjectListView.as_view(), name="projects_index"),
                       url(r'p/(?P<pk>\d+)/$', ProjectDetailView.as_view(), name="project_root"),
                       url(r'p/(?P<pk>\d+)/(?P<path>.*)$', project_fs, name="projects_fs")
                       #url(r'^tag/(?P<pk>\d+)/$'),
                       #url(r'^lang/(?P<pk>\d+)/')
                       )