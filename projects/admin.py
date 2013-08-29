from django.contrib import admin
from projects.models import LanguageTag, ProjectTag, Project

class LanguageTagAdmin(admin.ModelAdmin):
    pass

class ProjectTagAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(LanguageTag, LanguageTagAdmin)
admin.site.register(ProjectTag, ProjectTagAdmin)
admin.site.register(Project, ProjectAdmin)