import unittest

try:
    from selenium import webdriver
except ImportError:
    has_selenium = False
else:
    has_selenium = True

from django.test import LiveServerTestCase


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
