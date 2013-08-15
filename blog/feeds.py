# -*- coding: utf-8 -*-

from django.contrib.syndication.views import Feed
from blog.models import Article
import random


class BlogFeed(Feed):
    title = "Nakódeníčko a zápisníček feed"
    description = "Österreichischer Puppenmacher"
    link = "/blog/"

    def items(self):
        return Article.objects.order_by('-date_published')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        tags = item.tags.all()
        tags = [tag.name for tag in tags]
        if not tags:
            return random.choice([":", ";", "="]) + random.choice(["-", "●"]) + random.choice([")", "/", "(", "O"])
        else:
            return "Tags: " + ", ".join(tags)