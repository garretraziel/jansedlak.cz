from django.db import models


class ProjectTag(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class LanguageTag(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField("project url")
    summary = models.TextField()

    tags = models.ManyToManyField(ProjectTag)
    languages = models.ManyToManyField(LanguageTag)

    def __unicode__(self):
        return self.name