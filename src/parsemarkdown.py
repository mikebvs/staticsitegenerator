from textnode import TextNode, TextType
import re

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "```", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_url(nodes)
    return nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        #print(sections)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.NORMAL))
            else:
                split_nodes.append(TextNode(sections[i].lstrip("\n").rstrip("\n"), text_type)) # Strip \n for fenced code blocks
        new_nodes.extend(split_nodes)
    return new_nodes

def split_fenced_code_block(text):
    print("Input text:", repr(text))  # repr() shows whitespace characters
    parts = text.strip().split("```")
    print("Split parts:", parts)
    if len(parts) >= 2:
        content = parts[1]
        return [TextNode(content.strip(), TextType.CODE)]
    else:
        print("Warning: Invalid code block format")
        return [TextNode(text, TextType.NORMAL)]

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



        
        
        
        
        
        
        
        
        
       

