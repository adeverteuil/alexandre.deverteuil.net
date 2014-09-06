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
    url(r'', include('django.contrib.flatpages.urls')),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
