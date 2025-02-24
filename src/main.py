import textnode
import parsemarkdown
import blocktype
from markdown_parser import markdown_to_html_node, extract_title
from htmlnode import HTMLNode, ParentNode, LeafNode
import subprocess
import sys
import os
from pathlib import Path
def main():
    subprocess.call(['sh', './prep_public.sh'])
    #text_node = textnode.TextNode("Hello, world!", textnode.TextType.NORMAL, "http://example.com")


    #text_image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    #text_image = "This is text with a ![rick roll]() and ![obi wan]()"
    #print(parsemarkdown.extract_markdown_images(text_image))
    #text_link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    #text_link = "This is text with a link [to boot dev]() and [to youtube]()"
    #print(parsemarkdown.extract_markdown_url(text_link))

    #node = textnode.TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", textnode.TextType.NORMAL)
#
    #print(parsemarkdown.split_nodes_image(node))
#
    #node = textnode.TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", textnode.TextType.NORMAL)
#
    #print(parsemarkdown.split_nodes_url(node))

    #text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
#
    #print(parsemarkdown.text_to_textnodes(text))

    #text = "# WOW A HEADER\n\n1. ORDERED LIST 1\n\n2. ORDERED LIST 2\n\n3. ORDERED LIST 3\n\n* UNORDERED SNEAKY\n\n* MORE UNORDERED\n\n# MASSIVE HEADER\n\n## MORE HEADER"

    #text = "# A HEADER\n\n1. ORDERED LIST 1\n\n2. ORDERED LIST 2\n\n3. ORDERED LIST 3\n\n* UNORDERED LIST\n\n1. FAKE ORDERED LIST\n\n3. FAKE ORDERED LIST\n\n2. FAKE ORDERED LIST\n\n```CODE BLOCK```"
    #lines = parsemarkdown.markdown_to_blocks(text)
    #print(lines)
#
    #blocks = ['# A HEADER', '1. ORDERED LIST 1\n2. ORDERED LIST 2\n3. ORDERED LIST 3', '* UNORDERED LIST', '1. FAKE ORDERED LIST\n3. FAKE ORDERED LIST\n2. FAKE ORDERED LIST', '```CODE BLOCK```']
    #btype = blocktype.BlockType
    #for block in blocks:
    #    print(blocktype.BlockType.block_to_block_type(block))

    #blocks = ['# First Header', '## Second Header', '### Third Header', '#### Fourth Header', '##### Fifth Heder', '###### Sixth Header', '* Unordered List', '1. Ordered List 1', '15. Ordered List 2', '> Quote text', '`code text`','```\nBlock Code\n```']
    #for block in blocks:
    #    print(blocktype.BlockType.block_to_block_type(block))

    #markdown = "# h1 Heading\n\n## h2 Heading with **bold** text!\n\n### h3 Heading\n\n#### h4 Heading\n\n##### h5 Heading\n\n###### h6 Heading\n\nParagraph Text with *italics* as well as some **bold** text!\n\n'this is a paragraph with a [link](https://www.google.com) in it!\n\n* Unordered List\n\n* Unordered List Again\n\n- Another Unordered List Format\n\n1. Ordered List 1\n\n2. Ordered List 2\n\n```\nThis is a fenced code block\n```\n\na paragraph\nwith a new line\n\na paragraph with ![an image](https://imageurl.com)\n\nand a very cool `Code Block` wow check that out\n\n> Block Quote\n> Many Lines\n> Very important quote"
    #print(markdown_to_html_node(markdown))
    #extract_title(markdown)

    #print(os.path.abspath(os.curdir))
    ##new_dir = os.chdir('..')
    #print(os.getcwd())
    #levels = 2
    #path_up = os.path.join(*([os.pardir] * levels))
    #print(os.pardir)

    
    template_path = "template.html"
    root_dir = Path(__file__).parent.parent
    from_path = root_dir / "content"
    dest_path = root_dir / "public"
    generate_pages_recursive(from_path, template_path, dest_path)
    print(f"Main Finished.")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating a Static Page from {from_path} to {dest_path} using {template_path} as a Template.")
    
    print(f"Reading {from_path}...")
    file = open(from_path, 'r')
    from_content = file.read()
    file.close()
   
    print(f"Reading {template_path}...")
    file = open(template_path, 'r')
    template_content = file.read()
    file.close()
    
    print(f"Extracting Title...")
    title = extract_title(from_content)
    print(f"Converting markdown to HTMLNodes...")
    html_nodes = markdown_to_html_node(from_content)
    top_node = HTMLNode("div", None, html_nodes)
    print(f"Converting HTMLNodes into HTML...")
    html_content = top_node.to_html()
    print(f"Building File with HTML Template: {template_path}...")
    html_page = template_content.replace("{{ Title }}", title)
    html_page = template_content.replace("{{ Content }}", html_content)

    return html_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    #directories = get_all_directories(dir_path_content)
    files = get_all_files(dir_path_content)
    root_dir = Path(__file__).parent.parent

    # Iterate through all files found in the dir_path_content
    for file in files:
        # Initialize Path of file
        print(f"Initializing file paths for current document...")
        file_path = Path(file)
        # Get content root
        content_root = root_dir / "content"
        # Create HTML Page, if error no reason to create folders/files etc
        html_page = generate_page(file_path, template_path, dest_dir_path)
        # Compare file_path to content_root
        public_file_path = file_path.relative_to(content_root)
        # Build destination path with dest_dir_path and the file structure from public_file_path
        public_file_path = dest_dir_path / public_file_path
        # Create folder structure in dest_dir_path that is copied from file_path
        print(f"Creating directory: {public_file_path.parent}")
        public_file_path.parent.mkdir(parents=True, exist_ok=True)
        # Set new .html extension instead of .md
        file = public_file_path.stem
        file = file + ".html"
        # Build file path from public/ + the file structure (i.e. ./public + /majesty/index.html = ./public/majesty/index.html)
        file_dest = public_file_path.parent / file
        # Write file to folder location
        print(f"Writing HTML Content to file {file_dest}...")
        file_dest.write_text(html_page, encoding="utf-8")
        print(f"Successfully generated page.\n\n")
    return print(f"All valid pages generated.")

def get_all_directories(path_str):
    path = Path(path_str)
    return [x for x in path.iterdir() if x.is_dir()]

def get_all_files(path_str):
    path = Path(path_str)
    return [file for file in path.rglob("*") if file.is_file()]

if __name__ == "__main__": 
    main()