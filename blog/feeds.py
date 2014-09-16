from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse

from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "Le blogue d’Alexandre de Verteuil"
    link = "/blogue/"
    description = (
        "Billets récents publiés sur le blogue d’Alexandre de Verteuil"
        )

    def items(self):
        posts = Post.objects.order_by('-pub_date')
        return [post for post in posts if post.is_published()][:10]

    def item_title(self, item):
        return item.title  # TODO remove tags.

    def item_description(self, item):
        return item.summary  # TODO choose whether to display body instead.

    def item_link(self, item):
        return reverse('blog:detail', kwargs={'slug': item.slug})
