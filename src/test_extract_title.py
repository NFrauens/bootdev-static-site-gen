import unittest
from splitnodedelimiter import extract_title

class test_extract_title(unittest.TestCase):
    def test_extract_title_basic(self):
        markdown = "# Hello"
        title = extract_title(markdown)
        self.assertEqual("Hello", title)