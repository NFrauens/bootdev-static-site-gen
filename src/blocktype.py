from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown):
    new_text = []
    split_text = markdown.split("\n\n")
    for text in split_text:
        stripped_text = text.strip()
        if stripped_text == "":
            continue
        new_text.append(stripped_text)
    return new_text    

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