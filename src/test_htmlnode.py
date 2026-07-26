import unittest
from htmlnode import HTMLNode

class HTMLNode_Test1(unittest.TestCase):
    def test_none(self):
        test1 = HTMLNode()
        self.assertTrue(test1.props_to_html() == "")


    def test_2(self):
        test2 = HTMLNode("h1", "a", [1, 2, 3], {"href": "https://www.google.com","target": "_blank",})
        self.assertTrue(test2.props_to_html() == ' href="https://www.google.com" target="_blank"')


    def test_3(self):
        test3 = HTMLNode("h1", "a", [1, 2, 3], {"href": "https://www.google.com","target": "_blank",})
        self.assertFalse(test3.props_to_html() == None)

if __name__ == "__main__":
    unittest.main()