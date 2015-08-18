import datetime
import unittest

try:
    from selenium import webdriver
except ImportError:
    has_selenium = False
else:
    has_selenium = True

from django.test import LiveServerTestCase

from blog.models import Post


class IllegalStateException(Exception): pass


class PageObject:

    def __init__(self, selenium):
        self.selenium = selenium
        self.validate_page()

    def validate_page(self):
        if not self._validate_page():
            raise IllegalStateException(
                "Expected {}. Current url is \"{}\"".format(
                    self.__class__.__name__,
                    self.selenium.current_url,
                    )
                )


class HomePage(PageObject):

    def _validate_page(self):
        return self.selenium.title.startswith("Accueil")

    def go_to_blogue(self):
        l = self.selenium.find_element_by_link_text("Blogue")
        l.click()
        return BlogIndex(self.selenium)


class BlogIndex(PageObject):

    def _validate_page(self):
        return self.selenium.title.startswith("Blogue")

    def go_to_blog_post(self, title):
        l = self.selenium.find_element_by_link_text(title)
        l.click()
        return BlogPost(self.selenium, title=title)


class BlogPost(PageObject):

    def __init__(self, *args, title=None, **kwargs):
        assert title is not None
        self.title = title
        super().__init__(*args, **kwargs)

    def _validate_page(self):
        return self.title in self.selenium.title


@unittest.skipUnless(has_selenium, "Install selenium for front-end testing")
class BlogFrontEndTest(LiveServerTestCase):

    fixtures = ["starting_data"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        self.selenium.get(self.live_server_url)
        self.homepage = HomePage(self.selenium)

    def test_blog_index(self):
        blog_index = self.homepage.go_to_blogue()

    def test_empty_blog_index(self):
        Post.objects.all().delete()
        blog_index = self.homepage.go_to_blogue()
        body = blog_index.selenium.find_elements_by_tag_name("section")[0]
        self.assertIn("No posts are available.", body.text)

    def test_blog_index_with_one_entry_not_published(self):
        post = Post(
            title="Test_title_123",
            slug="test-title-123",
            pub_date=datetime.datetime(2015, 1, 1),
            public=False,
            )
        post.save()
        blog_index = self.homepage.go_to_blogue()
        body = blog_index.selenium.find_element_by_tag_name("section")
        self.assertIn("No posts are available.", body.text)

    def test_blog_index_with_one_entry_published(self):
        post = Post(
            title="Test_title_123",
            slug="test-title-123",
            pub_date=datetime.datetime(2015, 1, 1),
            public=True,
            )
        post.save()
        blog_index = self.homepage.go_to_blogue()
        body = blog_index.selenium.find_element_by_tag_name("section")
        self.assertNotIn("No posts are available.", body.text)
        self.assertIn("Test_title_123", body.text)

    def test_blog_title_in_breadcrumb(self):
        post = Post(
            title="Test_title_123",
            slug="test-title-123",
            pub_date=datetime.datetime(2015, 1, 1),
            public=True,
            )
        post.save()
        blog_index = self.homepage.go_to_blogue()
        blog_post = blog_index.go_to_blog_post("Test_title_123")
