import re
from textnode import TextNode, TextType

valid_delimiters = ["**", "_", "`",]


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    if delimiter not in valid_delimiters:
        raise Exception(f"invalid markdown syntax: {delimiter}")
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        temp_list = node.text.split(delimiter)
        if not len(temp_list) % 2:
            raise Exception("lone delimiter dectected")
        for i in range(len(temp_list)):
            if temp_list[i] == "":
                continue
            if i % 2:
                temp_str = TextNode(temp_list[i], text_type)
                new_nodes.append(temp_str)
                continue
            temp_str = TextNode(temp_list[i], TextType.TEXT)
            new_nodes.append(temp_str)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for current in old_nodes:
        if current.text_type != TextType.TEXT:
            new_nodes.append(current)
            continue

        ex_images = extract_markdown_images(current.text)

        if ex_images == []:
            new_nodes.append(current)
            continue

        original_text = current.text
        for tuple in ex_images:
            image_alt = tuple[0]
            image_link = tuple[1]
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for current in old_nodes:
        if current.text_type != TextType.TEXT:
            new_nodes.append(current)
            continue

        ex_links = extract_markdown_links(current.text)

        if ex_links == []:
            new_nodes.append(current)
            continue

        original_text = current.text
        for tuple in ex_links:
            link_alt = tuple[0]
            link_link = tuple[1]
            sections = original_text.split(f"[{link_alt}]({link_link})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link_alt, TextType.LINK, link_link))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    old_text = TextNode(text, TextType.TEXT)
    bold_delim = split_nodes_delimiter([old_text], "**", TextType.BOLD)
    italic_delim = split_nodes_delimiter(bold_delim, "_", TextType.ITALIC)
    code_delim = split_nodes_delimiter(italic_delim, "`", TextType.CODE)
    s_img = split_nodes_image(code_delim)
    s_link = split_nodes_link(s_img)
    return s_link

def markdown_to_blocks(markdown):
    new_text = []
    split_text = markdown.split("\n\n")
    for text in split_text:
        stripped_text = text.strip()
        if stripped_text == "":
            continue
        new_text.append(stripped_text)
    return new_text
