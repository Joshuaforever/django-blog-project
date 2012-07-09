"""
This code should be copy and pasted into blog/urls.py
"""


from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home'),
    url(r'^posts/$', 'blog.views.post_list'),
    url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'blog.views.post_detail'),
    ## add your url here
    url(r'^articles/2003/$', 'news.views.special_case_2003'),
    url(r'^articles/(\d{4})/$', 'news.views.year_archive'),
    url(r'^articles/(\d{4})/(\d{2})/$', 'news.views.month_archive'),
    url(r'^articles/(\d{4})/(\d{2})/(\d+)/$', 'news.views.article_detail'),
    posts/search/am
)
