# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Tag(models.Model):
    name = models.CharField("tag", max_length=255)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tag_index", kwargs={"pk":self.id})

    class Meta:
        verbose_name_plural = "tagy"


class Article(models.Model):
    title = models.CharField("nadpis", max_length=255)
    author = models.ForeignKey(User, verbose_name="autor")
    date_published = models.DateTimeField("datum", auto_now=True, editable=False)
    content = models.TextField("obsah")
    tags = models.ManyToManyField(Tag, blank=True, null=True, verbose_name="tagy")
    published = models.BooleanField("publikováno", default=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk":self.id})

    class Meta:
        verbose_name = "článek"
        verbose_name_plural = "články"
        ordering = ["-date_published", "title"]
