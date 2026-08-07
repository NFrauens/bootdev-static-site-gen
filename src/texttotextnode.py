from textnode import TextNode, TextType
from splitnodedeslimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    old_text = TextNode(text, TextType.TEXT)
    bold_delim = split_nodes_delimiter([old_text], "**", TextType.BOLD)
    italic_delim = split_nodes_delimiter(bold_delim, "_", TextType.ITALIC)
    code_delim = split_nodes_delimiter(italic_delim, "`", TextType.CODE)
    s_img = split_nodes_image(code_delim)
    s_link = split_nodes_link(s_img)
    return s_link
