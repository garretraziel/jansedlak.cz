from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.http import Http404
from django.contrib.auth.models import User
from blog.models import Article, Tag


class ArticleListView(ListView):
    context_object_name = "articles"
    queryset = Article.objects.filter(published=True).order_by('-date_published')
    paginate_by = 5
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context["authors"] = User.objects.annotate(num_articles=Count('article')).order_by('-num_articles')
        context["tags"] = Tag.objects.annotate(num_articles=Count('article')).order_by('-num_articles')
        return context


class TagListView(ListView):
    context_object_name = "articles"
    paginate_by = 5
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context["authors"] = User.objects.annotate(num_articles=Count('article')).order_by('-num_articles')
        context["tags"] = Tag.objects.annotate(num_articles=Count('article')).order_by('-num_articles')
        return context

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs["pk"])
        return tag.article_set.all()

    
class AuthorListView(ListView):
    context_object_name = "articles"
    paginate_by = 5
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context["authors"] = User.objects.annotate(num_articles=Count('article')).order_by('-num_articles')
        context["tags"] = Tag.objects.annotate(num_articles=Count('article')).order_by('-num_articles')
        return context

    def get_queryset(self):
        if User.objects.filter(username=self.kwargs["name"]).count() == 0:
            raise Http404
        queryset = Article.objects.filter(published=True).filter(author__username=self.kwargs["name"]).order_by('-date_published')
        return queryset
        

class ArticleDetailView(DetailView):
    context_object_name = "article"
    model = Article
    template_name = "blog/article.html"

    def get_object(self):
        article = super(ArticleDetailView, self).get_object()
        if not article.published and not self.request.user.has_perms('blog.add_article'):
            raise Http404
        return article
    
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context["authors"] = User.objects.annotate(num_articles=Count('article')).order_by('-num_articles')
        context["tags"] = Tag.objects.annotate(num_articles=Count('article')).order_by('-num_articles')
        return context
        
