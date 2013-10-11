from django.conf.urls import patterns, url


urlpatterns = patterns('apps.views',
    url(r'^$', 'application_list', name='application_list'),
    url(r'^([\w-]+)/$', 'application_list', name='application_list'),
    url(r'^([\w-]+)/([\w-]+)/$', 'application_detail', name='application_detail'),
)
