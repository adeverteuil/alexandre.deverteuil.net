import datetime

from django.test import TestCase

from blog.models import Post

class PostMethodTests(TestCase):

    def test_create_and_read_post(self):
        p1 = Post(
            title="test_create_post",
            pub_date=datetime.datetime(2014, 8, 1),
            body="This is the content",
            )
        p1.save()
        p2 = Post.objects.get(pk=p1.id)
        self.assertEqual(p1.title, p2.title)
        self.assertEqual(p1.id, p2.id)
        self.assertEqual(p1.pub_date, p2.pub_date)
        self.assertEqual(p1.body, p2.body)

    def test_mod_date(self):
        p1 = Post(
            title="foo title",
            pub_date=datetime.datetime(2014, 8, 1),
            body="This is the content",
            )
        p1.save()
        self.assertEqual(p1.mod_date(), p1.pub_date, msg=p1.mod_date())
        p2 = Post.objects.get(pk=p1.id)
        p2.body = "New content now."
        p2.save()
        p3 = Post.objects.get(pk=p1.id)
        self.assertNotEqual(p3.mod_date, p3.pub_date)
