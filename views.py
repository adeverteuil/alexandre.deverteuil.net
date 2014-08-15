from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from blog.models import Post


class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "latest_post_list"

    def get_queryset(self):
        """Return the last five published posts."""
        return Post.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/detail.html"
