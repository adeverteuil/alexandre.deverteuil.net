from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from links.models import Bookmark
from taggit.models import Tag


class BookmarkArchiveMixin:

    model = Bookmark
    context_object_name = "bookmarks"
    date_field = "datetime_added"
    paginate_by = 10
    allow_empty = True

    def get_queryset(self):
        queryset = super().get_queryset()
        tags = self.request.GET.getlist('tag')
        textfilter = self.request.GET.get('contains', None)
        for tag in tags:
            queryset = queryset.filter(tags__slug__in=[tag])
        if textfilter is not None:
            q = Q()
            for term in textfilter.split(" "):
                if term == "":
                    continue
                qq = Q(title__icontains=term)
                qq |= Q(description__icontains=term)
                qq |= Q(tags__name__in=[term])
                q &= qq
            queryset = queryset.filter(q).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tagslugs = self.request.GET.getlist('tag')
        if tagslugs:
            q = Q()
            for slug in tagslugs:
                q |= Q(slug=slug)
            context['querytags'] = Tag.objects.filter(q)
        return context


class BookmarkArchiveIndex(BookmarkArchiveMixin, ArchiveIndexView):

    pass


class BookmarkYearArchive(BookmarkArchiveMixin, YearArchiveView):

    make_object_list = True


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
