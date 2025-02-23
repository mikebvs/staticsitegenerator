import textnode
import parsemarkdown
import blocktype
import markdown_parser

def main():
    text_node = textnode.TextNode("Hello, world!", textnode.TextType.NORMAL, "http://example.com")


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

    markdown = "# h1 Heading\n\n## h2 Heading\n\n### h3 Heading\n\n#### h4 Heading\n\n##### h5 Heading\n\n###### h6 Heading\n\nParagraph Text\n\n* Unordered List\n\n1. Ordered List 1\n\n2. Ordered List 2\n\n```Code Block```\n\n> Block Quote"
    markdown_parser.markdown_to_html_node(markdown)

if __name__ == "__main__": 
    main()