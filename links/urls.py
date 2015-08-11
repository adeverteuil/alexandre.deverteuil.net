from django.conf.urls import patterns, url

from links.views import BookmarkArchiveIndex, BookmarkCreate, BookmarkUpdate, BookmarkDelete, BookmarkYearArchive

urlpatterns = patterns('',
    url(r"^$", BookmarkArchiveIndex.as_view(), name="bookmark_archive", kwargs={'page': 1, 'year': ""}),
    url(r"^page_(?P<page>[0-9]+)/$", BookmarkArchiveIndex.as_view(), name="bookmark_archive", kwargs={'year': ""}),
    url(r"^(?P<year>[0-9]+)/$", BookmarkYearArchive.as_view(), name="bookmark_archive", kwargs={'page': 1}),
    url(r"^(?P<year>[0-9]+)/page_(?P<page>[0-9]+)/$", BookmarkYearArchive.as_view(), name="bookmark_archive"),
    url(r"^bookmark/add/$", BookmarkCreate.as_view(), name="bookmark_add"),
    url(r"^bookmark/(?P<pk>[0-9]+)/$", BookmarkUpdate.as_view(), name="bookmark_update"),
    url(r"^bookmark/(?P<pk>[0-9]+)/delete/$", BookmarkDelete.as_view(), name="bookmark_delete"),
    )
