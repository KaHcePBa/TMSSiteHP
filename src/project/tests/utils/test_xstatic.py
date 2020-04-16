from pathlib import Path
from unittest import TestCase

from django.http import Http404
from django.http import HttpResponse

from project.utils.xstatic import get_favicon
from project.utils.xstatic import render_static


class MockFile:
    def __init__(self, data):
        self.__data = data

    def open(self, *_a, **_kw):
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return not exc_type

    def read(self):
        return self.__data

    def is_file(self):
        return True


class Test(TestCase):
    def test_get_favicon(self):
        ret = get_favicon()
        self.assertIsInstance(ret, Path)
        self.assertTrue(ret.is_file())
        self.assertEqual(ret.name, "favicon.png")

    def test_render_static(self):
        with self.assertRaises(Http404):
            render_static(Path("xxx"), "")

        ret = render_static(MockFile("XXX"), "text/css")
        self.assertIsInstance(ret, HttpResponse)
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.content, b"XXX")
        self.assertTrue(ret.has_header("Content-Type"))
        self.assertEqual(ret.get("Content-Type"), "text/css")
