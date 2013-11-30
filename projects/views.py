from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from projects.models import LanguageTag, ProjectTag, Project


class ProjectListView(ListView):
    context_object_name = "projects"
    queryset = Project.objects.order_by("name")
    template_name = "projects/index.html"


class ProjectDetailView(DetailView):
    context_object_name = "project"
    model = Project
    template_name = "projects/detail.html"
