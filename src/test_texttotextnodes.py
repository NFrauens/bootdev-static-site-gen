import unittest
from texttotextnode import text_to_textnodes
from textnode import TextNode, TextType

class Test_TexttoTextnodes(unittest.TestCase):
    def test_withalltypes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        converted_text = text_to_textnodes(text)
        self.assertEqual(converted_text,[
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

    def test_plaintextonly(self):
        text = "this is all plain text."
        converted_text = text_to_textnodes(text)
        self.assertEqual(converted_text,[
            TextNode("this is all plain text.", TextType.TEXT)
        ])

    def test_repeattype(self):
        text = "This is **bold** and this is **bold**"
        converted_text = text_to_textnodes(text)
        self.assertEqual(converted_text,[
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and this is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ])

    def test_adjacentdelimiters(self):
        text = "This is with **bold**_italic_ words next to each other."
        converted_text = text_to_textnodes(text)
        self.assertEqual(converted_text, [
            TextNode("This is with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode("italic", TextType.ITALIC),
            TextNode(" words next to each other.", TextType.TEXT),
        ])

    def test_onlyformatted(self):
        text = "_this is only italic_"
        converted_text = text_to_textnodes(text)
        self.assertEqual(converted_text, [
            TextNode("this is only italic", TextType.ITALIC),
        ])