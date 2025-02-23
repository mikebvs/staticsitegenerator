from textnode import TextNode, TextType
import re

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_url(nodes)
    return nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    # Iterate through all nodes in the old_nodes list
    for node in old_nodes:
        # If the node is not normal text, append it to the new_nodes list and continue to the next node
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            node.text.split(delimiter)
            delimiter_found = False
            # Check if delimiter exists in the text
            if delimiter in node.text:
                # Iterate through all instances of the delimiter in the text
                while delimiter in node.text:
                    # If we have detected a delimiter, we need to append the text before the delimiter as a normal text node
                    if delimiter_found == True:
                        new_nodes.append(TextNode(node.text.split(delimiter, maxsplit=1)[0], text_type))
                        node = TextNode(node.text.split(delimiter, maxsplit=1)[1], TextType.NORMAL)
                        delimiter_found = False
                    # If we have not detected a delimiter, we need to append the text before the delimiter as a normal text node
                    else:
                        new_nodes.append(TextNode(node.text.split(delimiter, maxsplit=1)[0], TextType.NORMAL))
                        node = TextNode(node.text.split(delimiter, maxsplit=1)[1], text_type)
                        delimiter_found = True
                # Append the remaining text as a normal text node
                new_nodes.append(node)
            # If the delimiter does not exist, just append the node to the new_nodes list            
            else:
                new_nodes.append(node)

    return new_nodes

def extract_markdown_images(text):
    # regex_pattern = re.compile(r'<img src="[^"]*" alt="[^"]*">', re.IGNORECASE)
    regex_pattern = re.compile(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", re.IGNORECASE)
    return re.findall(regex_pattern, text)

def extract_markdown_url(text):
    regex_pattern = re.compile(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", re.IGNORECASE)
    return re.findall(regex_pattern, text)

def split_nodes_image(old_nodes):
    new_nodes = []

    # Iterate through all nodes passed in
    for node in old_nodes:

        # Check for pre-formatted nodes
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        
        old_text = node.text

        # NodeText.text is empty, keep current NodeText
        if old_text == "":
            new_nodes.append(node)
            continue

        images = extract_markdown_images(old_text)
        # No Images to split, keep current NodeText
        if len(images) == 0:
            new_nodes.append(node)
            continue

        # Iterate through Image pairs
        for image in images:
            
            # Split text around each detected URL
            image_sections = old_text.split(f"![{image[0]}]({image[1]})", 1)

            # If pairs are not complete, raise error
            if len(image_sections) != 2:
                raise ValueError("Invalid Markdown, image section is not complete")
            
            # If there is text before your Image, create a valid TextNode with TextType.NORMAL
            if image_sections[0] != "":
                new_nodes.append(TextNode(image_sections[0], TextType.NORMAL))

            # If Image Destination is "" set it to None
            image_dest = None if image[1] == "" else image[1]
            
            # Append TextNode with TextType.LINK to new_nodes
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image_dest))

            old_text = image_sections[1]

        # if there is text after your Image, create a valid TextNode with TextType.NORMAL
        if old_text != "":
            new_nodes.append(TextNode(old_text, TextType.NORMAL))

    # Pass nodes to split_nodes_url in order to process leftover links
    return split_nodes_url(new_nodes)

def split_nodes_url(old_nodes):
    new_nodes = []

    # Iterate through all nodes passed in
    for node in old_nodes:
        # Check for pre-formatted nodes
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        old_text = node.text
        
        # NodeText.text is empty, keep current NodeText
        if old_text == "":
            new_nodes.append(node)
            continue

        urls = extract_markdown_url(old_text)
        # No URLs to split, keep current NodeText
        if len(urls) == 0:
            new_nodes.append(node)
            continue
        
        # Iterate through URL pairs
        for url in urls:
            
            # Split text around each detected URL
            url_sections = old_text.split(f"[{url[0]}]({url[1]})", 1)
            
            # If pairs are not complete, raise error
            if len(url_sections) != 2:
                raise ValueError("Invalid Markdown, url section is not complete")
            
            # If there is text before your URL, create a valid TextNode with TextType.NORMAL
            if url_sections[0] != "":
                new_nodes.append(TextNode(url_sections[0], TextType.NORMAL))
 
            # If URL Destination is "" set it to None
            url_dest = None if url[1] == "" else url[1]  

            # Append TextNode with TextType.LINK to new_nodes
            new_nodes.append(TextNode(url[0], TextType.LINK, url_dest))
            
            old_text = url_sections[1]

        # if there is text after your URL, create a valid TextNode with TextType.NORMAL
        if old_text != "":
            new_nodes.append(TextNode(old_text, TextType.NORMAL))

    return new_nodes
        
def markdown_to_blocks(md):
    blocks = md.split("\n\n")  # Split input by double newlines
    filtered_blocks = []
    block_to_add = ""

    for block in blocks:
        block = block.strip()  # Remove whitespace
        if not block:  # Skip empty blocks
            continue

        # Detect if block starts as an unordered list
        is_unordered = block.startswith("*")
        
        # Detect if block starts as an ordered list (e.g., "1.", "2.")
        is_ordered = re.match(r"^\d+[.)]", block)

        if (block_to_add and is_unordered and block_to_add.startswith("*")) or \
           (block_to_add and is_ordered and re.match(r"^\d+[.)]", block_to_add)):
            # Same list type, append current block to the grouped block
            block_to_add += "\n" + block
        else:
            # Finalize and add the last block to the result
            if block_to_add:
                filtered_blocks.append(block_to_add)
            # Start a new block
            block_to_add = block

    # Add the final block after the loop
    if block_to_add:
        filtered_blocks.append(block_to_add)

    return filtered_blocks



        
        
        
        
        
        
        
        
        
       

