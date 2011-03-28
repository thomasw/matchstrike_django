from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.views.static import serve

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.phtml'), name='index'),
    #(r'appname/', include('appname.urls')),
    url(r'^manage/', include(admin.site.urls)),
)

if getattr(settings, 'DEBUG'):
    urlpatterns += patterns('',
        url(r'^assets/(?P<path>.*)$', serve, {'document_root':getattr(settings,'MEDIA_ROOT')}),
    )