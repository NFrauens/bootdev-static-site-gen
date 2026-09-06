import unittest
from splitnodedelimiter import extract_title

class test_extract_title(unittest.TestCase):
    def test_extract_title_basic(self):
        markdown = "# Hello"
        title = extract_title(markdown)
        self.assertEqual("Hello", title)

    def test_extract_title_advanced(self):
        markdown = "# Hello\nWorld"
        title = extract_title(markdown)
        self.assertEqual("Hello", title)

    def test_extract_title_error(self):
        markdown = "Hello\nWorld"
        self.assertRaises(Exception, extract_title, markdown)

    def test_extract_title_twohash(self):
        markdown = "## Hello\nWorld"
        self.assertRaises(Exception, extract_title, markdown)