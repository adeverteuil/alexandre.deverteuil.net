import datetime

from django.core.management.base import BaseCommand, CommandError

from bs4 import BeautifulSoup
import pytz

from links.models import Bookmark


class Command(BaseCommand):

    help = "Import bookmarks from Shaarli"
    args = "<filename>"

    def handle(self, *args, **options):
        self.filename = args[0]
        self.options = options
        self.soup = self.get_soup()
        self._import()

    def get_soup(self):
        with open(self.filename) as f:
            soup = BeautifulSoup(f, "html5lib")
        return soup

    def _import(self):
        for tag in self.soup.body.children:
            if tag.name == "dt":
                d = {}
                d['title'] = str(tag.a.string)
                d['url'] = tag.a['href']
                date = datetime.datetime.fromtimestamp(
                    int(tag.a['add_date'])
                    )
                d['datetime_added'] = date
                d['datetime_modified'] = date
                d['private'] = tag.a['private'] == "1"
                if 'tags' in tag.a.attrs:
                    d['tags'] = tag.a['tags']
                if tag.next_sibling.name == "dd":
                    d['description'] = str(tag.next_sibling.string).strip()
                self.add_bookmark(d)

    def add_bookmark(self, d):
        tags = d.pop('tags', None)
        bookmark = Bookmark(**d)
        bookmark.save()
        bookmark.datetime_added = d['datetime_added']
        bookmark.save()
        if tags is not None:
            for t in tags.split(','):
                bookmark.tags.add(t)
        print(bookmark.title, bookmark.url)
