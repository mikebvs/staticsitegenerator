from htmlnode import HTMLNode, ParentNode, LeafNode
from blocktype import BlockType, block_to_block_type
from parsemarkdown import markdown_to_blocks, text_to_textnodes
from textnode import TextNode, text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    #print(blocks)
    html_blocks = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.ORDERED_LIST:
            html_blocks.append(ol_block_to_html_node(block))
        elif block_type == BlockType.UNORDERED_LIST:
           html_blocks.append(ul_block_to_html_node(block))
        elif block_type == BlockType.CODE:
            html_blocks.append(code_block_to_html_node(block))
        elif block_type == BlockType.HEADING:
            html_blocks.append(heading_to_html_node(block))
        elif block_type == BlockType.QUOTE:
            html_blocks.append(quote_to_html_block(block))
        elif block_type == BlockType.PARAGRAPH:
            html_blocks.append(paragraph_to_html_block(block))


        
    print(f"\n\n\n\n{html_blocks}")
    
     
    return html_blocks

def paragraph_block_to_paragraph_html_node(block):
    #print(block)
    return None

def process_ordered_list(block):
    processed_blocks = []
    block_list = block.split("\n")
    for blocks in block_list:
        temp_list = blocks.split(". ")
        temp_list.pop(0)
        processed_blocks.append(" ".join(temp_list))
    return processed_blocks

def ol_block_to_html_node(block):
    # Create Container
    list_node = ParentNode("ol", [])
    # Clean Ordered List blocks with helper function
    ordered_list = process_ordered_list(block)
    # Iterate through each Ordered List Item
    for ol in ordered_list:
        # Convert to TextNodes   
        text_nodes = text_to_textnodes(ol)
        html_nodes = []
        # Iterate through TextNodes
        for text_node in text_nodes:
            # Convert TextNode to ParentNode
            html_node = text_node_to_html_node(text_node)
            # Add to  html_nodes
            html_nodes.append(html_node)
        # Wrap in <li> tag
        li_node = ParentNode("li", None, html_nodes)
        # Append children of <ol> container
        list_node.children.append(li_node)
    return list_node

def process_unordered_list(block):
    processed_blocks = []
    block_list = block.split("\n")
    for blocks in block_list:
        processed_blocks.append(blocks[2:])
    return processed_blocks

def ul_block_to_html_node(block):
    # Create Container
    ul_list_node = ParentNode("ul", [])
    # Clean Unordered List blocks with helper function
    ul_list = process_unordered_list(block)
    # Iterate through each Unordered List Item
    for ul in ul_list:
        # Convert to TextNode
        text_nodes = text_to_textnodes(ul)
        html_nodes = []
        # Iterate through TextNodes
        for text_node in text_nodes:
            # Convert TextNode to ParentNode
            html_node = text_node_to_html_node(text_node)
            # Add to html_nodes
            html_nodes.append(html_node)
        # Wrap in <li> tags
        li_node = ParentNode("li", None, html_nodes)
        # Append children of <ul> container
        ul_list_node.children.append(li_node)
    return ul_list_node

def code_block_to_html_node(block):
    text_node = text_to_textnodes(block)
    html_children = []
    for node in text_node:
        html_node = text_node_to_html_node(node)
        html_children.append(html_node)
    return ParentNode("pre", html_children)

def heading_to_html_node(block):
    block_list = block.split()
    heading_count = len(block_list[0])
    block_list.pop(0)
    stripped_text = " ".join(block_list)
    text_nodes = text_to_textnodes(stripped_text)
    html_children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        html_children.append(html_node)
    html_tag = "h" + str(heading_count)
    return ParentNode(html_tag, html_children)

def quote_to_html_block(block):
    quote_node = ParentNode("blockquote", [])
    html_children = []
    new_blocks = []
    for quote in block.split("\n"):
        new_line = quote.split()
        new_line.pop(0)
        new_line = " ".join(new_line)
        new_blocks.append(new_line)
    for qte in new_blocks:
        text_nodes = text_to_textnodes(qte)
        for tnode in text_nodes:
            html_node = text_node_to_html_node(tnode)
            html_children.append(html_node)
    p_nodes = ParentNode("p", html_children)
    quote_node.children.append(p_nodes)
    return quote_node

def paragraph_to_html_block(block):
    outer_node = ParentNode("p", [])
    blocks = block.split("\n")
    html_children = []
    for blk in blocks:
        text_nodes = text_to_textnodes(blk)
        for tnode in text_nodes:
            html_node = text_node_to_html_node(tnode)
            html_children.append(html_node)
    outer_node.children.append(html_children)
    return outer_node