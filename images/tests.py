import os.path

from django.test import TestCase
from django.conf import settings

from images.models import Image, Collection


class TestCollection(TestCase):

    def test_init(self):
        c = Collection(
            name="Test",
            slug="test",
            )
        c.save()
        self.assertTrue(c.pk)


class TestImages(TestCase):

    def setUp(self):
        c = Collection(name="Test", slug="test")
        c.save()
        self.imagefile = os.path.join(settings.MEDIA_ROOT, "image.jpg")
        open (self.imagefile, "wb").close()
        print(self.imagefile)
    
    def test_init(self):
        c = Collection.objects.first()
        i = Image(
            title="Test title",
            slug="test-slug",
            collection_id=c.pk,
            original=self.imagefile,
            )
        i.save()
        #self.assert
