from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alexdev.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^blogue/', include('blog.urls', namespace="blog")),
    url(r'^admin/', include(admin.site.urls)),
    )


# http://chriskief.com/2014/03/28/previewing-django-error-pages/
# Adding this before flatpages if in DEBUG mode.
if settings.DEBUG:
    from django.views.generic import TemplateView
    urlpatterns += patterns('',
        url(r'^400/$', TemplateView.as_view(template_name="400.html")),
        url(r'^403/$', TemplateView.as_view(template_name="403.html")),
        url(r'^404/$', TemplateView.as_view(template_name="404.html")),
        url(r'^500/$', TemplateView.as_view(template_name="500.html")),
        )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,
        )


urlpatterns += patterns('',
    url(r'', include('django.contrib.flatpages.urls')),
    )
