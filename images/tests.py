import os
import os.path
import shutil
import tempfile

from django.test import TestCase
from django.conf import settings

from images.models import Image


class TestImage(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        pass

    def test_create_given_file_exists(self):
        pass

    def test_create_given_file_not_exists(self):
        pass

    def test_create_given_basename_field_blank(self):
        pass

    def test_create_given_basename_field_not_blank(self):
        pass

    def test_read_given_normal_situation(self):
        pass

    def test_read_given_file_vanished(self):
        pass

    def test_read_given_dir_vanished(self):
        pass

    def test_update_basename(self):
        pass

    def test_update_basename_given_file_vanished(self):
        pass

    def test_update_basename_given_dest_exists(self):
        pass

    def test_update_basename_given_basename_field_is_blank(self):
        pass

    def test_update_collection(self):
        pass

    def test_update_collection_given_dir_not_exists(self):
        pass

    def test_update_collection_given_file_vanished(self):
        pass

    def test_update_collection_given_dest_exists(self):
        pass

    def test_update_original(self):
        pass

    def test_update_original_given_original_vanished(self):
        pass

    def test_update_original_given_same_file_uploaded(self):
        pass

    def test_update_both_collection_and_basename(self):
        pass

    def test_update_when_collection_is_renamed(self):
        pass

    def test_delete(self):
        pass

    def test_delete_given_file_vanished(self):
        pass

    def test_delete_given_collection_dir_vanished(self):
        pass
