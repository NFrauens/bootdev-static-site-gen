import unittest
from markdowntohtmlnode import markdown_to_html_node

class Test_markdowntohtmlnode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

    def test_headingwith6(self):
        md = "###### This is a title block with six leading hashtags"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>This is a title block with six leading hashtags</h6></div>"
        )

    def test_headingwith1(self):
        md = "# This is a title block with one leading hashtag"
    
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a title block with one leading hashtag</h1></div>"
        )

    def test_quoteblock(self):
        md = "> this\n> is\n> a\n> quote"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>this is a quote</blockquote></div>"
        )

    def test_unordered_list(self):
        md = "- this\n- is\n- a\n- list"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>this</li><li>is</li><li>a</li><li>list</li></ul></div>"
        )

    def test_ordered_list(self):
        md = "1. this\n2. is\n3. a\n4. list"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>this</li><li>is</li><li>a</li><li>list</li></ol></div>"
        )

    def test_multiple_types_one_block(self):
        md = "### Heading\n\n> quote\n\n- ul\n\n1. ol\n\nparagraph"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>Heading</h3><blockquote>quote</blockquote><ul><li>ul</li></ul><ol><li>ol</li></ol><p>paragraph</p></div>"
        )