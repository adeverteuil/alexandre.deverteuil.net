import datetime
import re
from pprint import pprint

from django.core.management.base import BaseCommand, CommandError
from blog.models import Post, Category


class Command(BaseCommand):

    args = '<post1.html post2.html ...>'
    help = 'Imports blog posts from pelican html files'

    def handle(self, *args, **options):
        for filename in args:
            self.stdout.write("Reading {}".format(filename))
            defaults = parse(filename)
            categories = defaults.pop('categories')
            title = defaults.pop('title')
            #print(title)
            #print(categories)
            #pprint(defaults)
            # Implement update_or_create only available when 1.7 is out.
            try:
                post = Post.objects.get(title=title)
                for key, value in defaults.items():
                    setattr(post, key, value)
                post.save()
                self.stdout.write("Updated article {}".format(post.title))
            except Post.DoesNotExist:
                defaults.update({'title': title})
                post = Post(**defaults)
                post.save()
                self.stdout.write("Created article {}".format(post.title))
            for cat_name in categories:
                try:
                    post.categories.get(name=cat_name)
                    self.stdout.write("Fount category {}.".format(cat_name))
                except Category.DoesNotExist:
                    try:
                        category = Category.objects.get(name=cat_name)
                        post.categories.add(category)
                        self.stdout.write(
                            "Assigned category {}.".format(cat_name)
                            )
                    except Category.DoesNotExist:
                        post.categories.create(name=cat_name)
                        self.stdout.write(
                            "Created category {}".format(cat_name)
                            )


def parse(filename):
    with open(filename) as file:
        defaults = {
            'public': True,
            'categories': [],
            'body': "",
            'title': "",
            'summary': "",
            'pub_date': datetime.datetime.now(),
            }
        body_lines = []
        in_body = False
        for line in file:
            if in_body:
                if line == "</body>\n":
                    in_body = False
                else:
                    body_lines.append(line)
            elif line == "<body>\n":
                in_body = True
            elif "<title>" in line:
                #   <title>soup</title>
                defaults['title'] = re.search(
                    r"(?<=<title>)[^<]*(?=</title>)", line
                    ).group()
            elif "<meta name=\"desc\"" in line:
                #   <meta name="desc" contents="soup" />
                defaults['summary'] = re.search(
                    r"(?<=contents=\")[^\"]*(?=\" ?/>)", line
                    ).group()
            elif "<meta name=\"date\"" in line:
                #   <meta name="date" contents="2014-03-13 21:00" />
                # Some files have seconds so we count 16 characters.
                #   <meta name="date" contents="2014-03-13 21:00:00" />
                defaults['pub_date'] = datetime.datetime.strptime(
                    re.search(
                        r"(?<=contents=\")[^\"]{16}", line
                        ).group(),
                    "%Y-%m-%d %H:%M",
                    )
            elif "<meta name=\"tags\"" in line:
                #   <meta name="tags" contents="2014-03-13 21:00" />
                defaults['categories'] = re.search(
                    r"(?<=contents=\")[^\"]*(?=\" ?/>)", line
                    ).group().split(", ")
        defaults['body'] = "".join(body_lines)
        return defaults
