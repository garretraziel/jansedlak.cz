from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from projects.models import LanguageTag, ProjectTag, Project


class ProjectIndexMixin(object):
    context_object_name = "projects"
    template_name = "projects/index.html"


class ProjectListView(ProjectIndexMixin, ListView):
    queryset = Project.objects.order_by("name")


class ProjectDetailView(DetailView):
    context_object_name = "project"
    model = Project
    template_name = "projects/detail.html"


class ProjectTagListView(ProjectIndexMixin, ListView):
    def get_queryset(self):
        tag = get_object_or_404(ProjectTag, pk=self.args["pk"])
        return tag.project_set.all()


class ProjectLanguageListView(ProjectIndexMixin, ListView):
    def get_queryset(self):
        lang = get_object_or_404(ProjectTag, pk=self.args["pk"])
        return lang.project_set.all()