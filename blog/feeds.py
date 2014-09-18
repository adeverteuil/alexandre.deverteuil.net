import datetime

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse

from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "Le blogue d’Alexandre de Verteuil"
    link = "/blogue/"
    title_template = "blog/feed_title.html"
    description_template = "blog/feed_description.html"
    description = (
        "Billets récents publiés sur le blogue d’Alexandre de Verteuil"
        )

    def items(self):
        now = datetime.datetime.now()
        return Post.objects.filter(
            pub_date__lte=now,
            public=True,
            ).order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return reverse('blog:detail', kwargs={'slug': item.slug})
