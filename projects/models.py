# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models
from django.core.urlresolvers import reverse


class ProjectTag(models.Model):
    name = models.CharField("jméno", max_length=255)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("project_tag", kwargs={"pk": self.id})

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tagy"


class LanguageTag(models.Model):
    name = models.CharField("jméno", max_length=255)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("language_tag", kwargs={"pk": self.id})

    class Meta:
        verbose_name = "jazyk"
        verbose_name_plural = "jazyky"


class Project(models.Model):
    name = models.CharField("jméno", max_length=255, unique=True)
    url = models.URLField("odkaz", null=True, blank=True)
    summary = models.TextField("souhrn")
    tarball = models.FileField(upload_to=lambda instance, filename: "projects/"+filename, null=True, blank=True)

    tags = models.ManyToManyField(ProjectTag, verbose_name="tagy")
    languages = models.ManyToManyField(LanguageTag, verbose_name="jazyky")

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return self.url

    def clean(self):
        if self.url is None and self.tarball is None:
            raise ValidationError("Musí být poskytnut tarball nebo link.")

    class Meta:
        verbose_name = "projekt"
        verbose_name_plural = "projekty"