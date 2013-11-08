from django.conf.urls import patterns, url


urlpatterns = patterns('comparisons.views',
    url(r'^$', 'detail', name='comparison_detail'),
    url(r'^([\w-]+)/$', 'detail', name='comparison_detail'),
)
