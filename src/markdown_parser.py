from htmlnode import HTMLNode
from blocktype import BlockType, block_to_block_type
from parsemarkdown import markdown_to_blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        print(block_to_block_type(block))
        if block_to_block_type(block) == BlockType.PARAGRAPH:
            paragraph_block_to_paragraph_html_node(block)

    #print(blocks)
    return None

def paragraph_block_to_paragraph_html_node(block):
    
    return None