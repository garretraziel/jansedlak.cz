from django.conf.urls import patterns, url
from blog.views import ArticleListView, TagListView, ArticleDetailView, AuthorListView

urlpatterns = patterns('blog.views',
                       url(r'^$', ArticleListView.as_view(), name='blog_index'),
                       url(r'^tag/(?P<pk>\d+)/$', TagListView.as_view(), name='tag_index'),
                       url(r'^(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='article_detail'),
                       url(r'^author/(?P<name>[^/]+)/$', AuthorListView.as_view(), name='author_list'),
                       )
