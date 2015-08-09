from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from links.models import Bookmark
from taggit.models import Tag


class BookmarkList(ListView):

    model = Bookmark
    paginate_by = 10


class LoginRequiredMixin:

    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return login_required(view)


class BookmarkCreate(LoginRequiredMixin, CreateView):

    model = Bookmark
    fields = ("url", "title", "private", "description", "tags")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all().order_by("name")
        return context


class BookmarkUpdate(LoginRequiredMixin, UpdateView):

    model = Bookmark
    fields = ("url", "title", "private", "description", "tags")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all().order_by("name")
        return context


class BookmarkDelete(LoginRequiredMixin, DeleteView):

    model = Bookmark
    success_url = reverse_lazy("links:bookmark_list")
