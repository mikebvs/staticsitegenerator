from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

    def block_to_block_type(markdown_block):
        if markdown_block != "":
            regex_pattern = re.compile(r"[0-9]+\. ", re.IGNORECASE)
            block_start = markdown_block.split()[0]
            block_end = markdown_block.split()[len(markdown_block)-1]
            if block_start == "#":
                return BlockType.HEADING
            elif block_start == "##":
                return BlockType.HEADING
            elif block_start == "###":
                return BlockType.HEADING
            elif block_start == "####":
                return BlockType.HEADING
            elif block_start == "#####":
                return BlockType.HEADING
            elif block_start == "######":
                return BlockType.HEADING
            elif block_start == "*":
                return BlockType.UNORDERED_LIST
            elif block_start == "-":
                return BlockType.UNORDERED_LIST
            elif block_start == ">":
                return BlockType.QUOTE
            elif block_start == "```" and block_end == "```":
                return BlockType.CODE
            elif re.match(regex_pattern, markdown_block):
                return BlockType.ORDERED_LIST
            else:
                return BlockType.PARAGRAPH
        
        return BlockType.PARAGRAPH