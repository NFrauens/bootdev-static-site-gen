from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
                return True
        return False

    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type.value}, {self.url})")

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise Exception("not a valid text type")

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(md: str) -> BlockType:
    original_str = md
 
    if original_str[:2] == "# " or original_str[:3] == "## " or original_str[:4] == "### " or original_str[:5] == "#### " or original_str[:6] == "##### " or original_str[:7] == "###### ":
        return BlockType.HEADING

    elif original_str[:4] == "```\n" and original_str[-3:] == "```":
        return BlockType.CODE

    elif original_str[:1] == ">":
        split_str = original_str.split("\n")
        str_number = len(split_str)
        match_num = 0
        for line in split_str:
            if line[:1] == ">":
                match_num += 1
        if str_number == match_num:
            return BlockType.QUOTE
        return BlockType.PARAGRAPH
    
    elif original_str[:2] == "- ":
        split_str = original_str.split("\n")
        str_number = len(split_str)
        match_num = 0
        for line in split_str:
            if line[:2] == "- ":
                match_num += 1
        if str_number == match_num:
            return BlockType.UNORDERED_LIST
        return BlockType.PARAGRAPH

    elif original_str[:3] == "1. ":
        split_str = original_str.split("\n")
        line_number = 1
        for line in split_str:
            if not line.startswith(f"{line_number}. "):
                return BlockType.PARAGRAPH
            line_number += 1
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH