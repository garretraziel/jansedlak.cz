from django.conf.urls import patterns, url
from projects.views import ProjectListView, ProjectDetailView, ProjectTagListView, ProjectLanguageListView

urlpatterns = patterns('projects.views',
                       url(r'^$', ProjectListView.as_view(), name="projects_index"),
                       url(r'p/(?P<pk>\d+)/$', ProjectDetailView.as_view(), name="project_root"),
                       url(r'^tag/(?P<pk>\d+)/$', ProjectTagListView.as_view(), name="project_tag"),
                       url(r'^lang/(?P<pk>\d+)/', ProjectLanguageListView.as_view(), name="project_language")
                       )