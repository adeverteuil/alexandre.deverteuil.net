from django.conf.urls import patterns, url

from links.views import BookmarkList, BookmarkCreate, BookmarkUpdate, BookmarkDelete

urlpatterns = patterns('',
    url(r"^$", BookmarkList.as_view(), name="bookmark_list", kwargs={'page': 1}),
    url(r"^page_(?P<page>[0-9]+)/$", BookmarkList.as_view(), name="bookmark_list"),
    url(r"^bookmark/add/$", BookmarkCreate.as_view(), name="bookmark_add"),
    url(r"^bookmark/(?P<pk>[0-9]+)/$", BookmarkUpdate.as_view(), name="bookmark_update"),
    url(r"^bookmark/(?P<pk>[0-9]+)/delete/$", BookmarkDelete.as_view(), name="bookmark_delete"),
    )
