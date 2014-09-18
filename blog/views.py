import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from blog.models import Post


class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "latest_post_list"

    def get_queryset(self):
        """Return the published posts."""
        now = datetime.datetime.now()
        return Post.objects.filter(
            pub_date__lte=now,
            public=True,
            ).order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/detail.html"
