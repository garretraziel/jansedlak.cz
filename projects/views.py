from django.views.generic import ListView, DetailView
from projects.models import LanguageTag, ProjectTag, Project


class ProjectListView(ListView):
    context_object_name = "projects"
    queryset = Project.objects.order_by("name")
    template_name = "projects/index.html"
