from django.conf.urls import patterns, url

from blog import views, feeds

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^rss/$', feeds.LatestEntriesFeed(), name="rss"),
    url(
        r'^(?P<slug>[-_a-z0-9]+)/$',
        views.DetailView.as_view(),
        name="detail",
        ),
    )
