# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models


class ProjectTag(models.Model):
    name = models.CharField("jméno", max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tagy"


class LanguageTag(models.Model):
    name = models.CharField("jméno", max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "jazyk"
        verbose_name_plural = "jazyky"


class Project(models.Model):
    name = models.CharField("jméno", max_length=255)
    url = models.URLField("project url")
    summary = models.TextField("souhrn")

    tags = models.ManyToManyField(ProjectTag, verbose_name="tagy")
    languages = models.ManyToManyField(LanguageTag, verbose_name="jazyky")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "projekt"
        verbose_name_plural = "projekty"