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
