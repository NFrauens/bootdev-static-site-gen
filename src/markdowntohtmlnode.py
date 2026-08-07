from blocktype import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import HTMLNode, LeafNode, ParentNode
from texttotextnode import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_node_list = []
    for block in blocks:
        typed_block = block_to_block_type(block)
        if typed_block == BlockType.PARAGRAPH:
            html_node_list.append(paragraph_block(block))
        elif typed_block == BlockType.HEADING:
            html_node_list.append(heading_block(block))
        elif typed_block == BlockType.QUOTE:
            html_node_list.append(quote_block(block))
        elif typed_block == BlockType.UNORDERED_LIST:
            html_node_list.append(unordered_list_block(block))
        elif typed_block == BlockType.ORDERED_LIST:
            html_node_list.append(ordered_list_block(block))
        elif typed_block == BlockType.CODE:
            html_node_list.append(code_block(block))
    parent = ParentNode("div", html_node_list)
    return parent


def text_to_children(text: str):
    old_list = text_to_textnodes(text)
    new_list = []
    for node in old_list:
        new_list.append(text_node_to_html_node(node))
    return new_list

def paragraph_block(block):
    replaced_block = block.replace("\n", " ")
    stripped_block = replaced_block.strip()
    children = text_to_children(stripped_block)
    parent = ParentNode("p", children)
    return parent

def heading_block(block):
    lstripped_block = block.lstrip("#")
    stripped_block = lstripped_block.strip()
    children = text_to_children(stripped_block)
    parent = ParentNode(f"h{(len(block) - len(lstripped_block))}", children)
    return parent

def quote_block(block):
    line_list = block.split("\n")
    new_line_list = []
    for line in line_list:
        remove_gthan = line.replace(">", "")
        removed_whitespace = remove_gthan.strip()
        new_line_list.append(removed_whitespace)
    reconstructed_text = ""
    for new_line in new_line_list:
        reconstructed_text = reconstructed_text + f"{new_line}" + " "
    final_text = reconstructed_text.strip()
    children = text_to_children(final_text)
    parent = ParentNode("blockquote", children)
    return parent

def unordered_list_block(block):
    line_list = block.split("\n")
    per_line_node_list = []
    for line in line_list:
        remove_dash = line[2:]
        remove_whitespace = remove_dash.strip()
        children = text_to_children(remove_whitespace)
        parent = ParentNode("li", children)
        per_line_node_list.append(parent)
    final_parent = ParentNode("ul", per_line_node_list)
    return final_parent

def ordered_list_block(block):
    line_list = block.split("\n")
    per_line_node_list = []
    for line in line_list:
        remove_line_number = line[(line.find(". ") + 2):]
        remove_whitespace = remove_line_number.strip()
        children = text_to_children(remove_whitespace)
        parent = ParentNode("li", children)
        per_line_node_list.append(parent)
    final_parent = ParentNode("ol", per_line_node_list)
    return final_parent

def code_block(block):
    lsliced_block = block[3:]
    rsliced_block = lsliced_block[:-3]
    remove_l_whitespace = rsliced_block.lstrip()
    code_textnode = TextNode(remove_l_whitespace, TextType.CODE)
    code_htmlnode = text_node_to_html_node(code_textnode)
    parent = ParentNode("pre", [code_htmlnode])
    return parent