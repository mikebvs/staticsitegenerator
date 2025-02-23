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
            elif markdown_block.startswith("```") and markdown_block.endswith("```"):# and block_end == "```":
                return BlockType.CODE
            elif markdown_block[0] == '`' and markdown_block[1] != '`':
                return BlockType.CODE
            elif re.match(regex_pattern, markdown_block):
                # Split markdown_block into a list of lines
                list_items = markdown_block.split("\n")
                ordered_list_iterator = 0
                # Iterate through items to verify that it starts with "1. " and increments by 1 each time (i.e "1. ", "2. ", "3. ")
                for l_item in list_items:
                    # If l_item starts with "#. "
                    if re.match(regex_pattern, l_item):

                        # Handle first item in list_items                        
                        if ordered_list_iterator == 0:
                            # Check if ordered list correctly begins with "1. "
                            if l_item.split()[0] == "1.":
                                ordered_list_iterator = 1     
                            # Return BlockType.PARAGRAPH if the Ordered List does not begin with "1. "
                            else:
                                return BlockType.PARAGRAPH
                        # Handle items after the first
                        else:
                            # Iterate ordered list iterator to compare to current l_item list number
                            ordered_list_iterator += 1
                            # Check if the new list item's leading number is equal to ordered_list_iterator, if not return BlockType.PARAGRAPH
                            if int(l_item.split()[0].split(".")[0]) != ordered_list_iterator:
                                return BlockType.PARAGRAPH
                            
                    # Regex Function did not match, return BlockType.PARAGRAPH
                    else:
                        return BlockType.PARAGRAPH
                # After successfully iterating through all lines in the markdown_block, return BlockType.ORDERED_LIST
                return BlockType.ORDERED_LIST
            
            else:
                return BlockType.PARAGRAPH  
        return BlockType.PARAGRAPH