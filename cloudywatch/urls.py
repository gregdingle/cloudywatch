from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'apps.views.index', name='index'),
    (r'^apps/', include('apps.urls')),
    url(r'^admin/find-tool/$', 'apps.views.foo', name='foo'),

    (r'^admin/', include(admin.site.urls)),
   
    (r'^ckeditor/', include('ckeditor.urls')),
    
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
