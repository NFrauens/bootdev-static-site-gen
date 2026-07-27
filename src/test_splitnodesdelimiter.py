import unittest
from splitnodedeslimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class Test_splitnodesdelimter(unittest.TestCase):
    def testcodesplit(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),TextNode("code block", TextType.CODE),TextNode(" word", TextType.TEXT),])

    def testboldsplit(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),TextNode("bold block", TextType.BOLD),TextNode(" word", TextType.TEXT),])

    def testitalicsplit(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),TextNode("italic block", TextType.ITALIC),TextNode(" word", TextType.TEXT),])

    def testmultiplenodes(self):
        nodecode = TextNode("This is text with a `code block` word", TextType.TEXT)
        nodebold = TextNode("**bold block**", TextType.BOLD)
        nodeitalic = TextNode("_italic block_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter([nodecode, nodebold, nodeitalic], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),TextNode("code block", TextType.CODE),TextNode(" word", TextType.TEXT), nodebold, nodeitalic,])

    def testlonedelimiter(self):  
        node = TextNode("this is a `lone delimter", TextType.TEXT)
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "`", TextType.TEXT)

    def testlonedelimiter2(self):  
        node = TextNode("this is a `lone delimter` and `another", TextType.TEXT)
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "`", TextType.TEXT)

    def testonlybold(self):
        nodebold1 = TextNode("bold", TextType.BOLD)
        nodebold2 = TextNode("bold2", TextType.BOLD)
        nodebold3 = TextNode("bold3", TextType.BOLD)
        new_nodes = split_nodes_delimiter([nodebold1, nodebold2, nodebold3], "`", TextType.TEXT)
        self.assertEqual(new_nodes, [nodebold1, nodebold2, nodebold3])

    def testemptystring(self):
        node = TextNode("`code` string", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("code", TextType.CODE), TextNode(" string", TextType.TEXT)])