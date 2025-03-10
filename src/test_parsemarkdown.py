import unittest

from textnode import TextNode, TextType
from parsemarkdown import *


class TestParseMarkdown(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("This is text with a `code block` word. omg two `code blocks` wow!", TextType.NORMAL)
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), [TextNode("This is text with a ", TextType.NORMAL), TextNode("code block", TextType.CODE), TextNode(" word. omg two ", TextType.NORMAL), TextNode("code blocks", TextType.CODE), TextNode(" wow!", TextType.NORMAL)])

    def test_bold(self):
        node = TextNode("This is text with a **BOLD** word. omg two **BOLD** wow!", TextType.NORMAL)
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), [TextNode("This is text with a ", TextType.NORMAL), TextNode("BOLD", TextType.BOLD), TextNode(" word. omg two ", TextType.NORMAL), TextNode("BOLD", TextType.BOLD), TextNode(" wow!", TextType.NORMAL)])

    def test_itatic(self):
        node = TextNode("This is text with a *italic* word. omg two *italic* wow!", TextType.NORMAL)
        self.assertEqual(split_nodes_delimiter([node], "*", TextType.ITALIC), [TextNode("This is text with a ", TextType.NORMAL), TextNode("italic", TextType.ITALIC), TextNode(" word. omg two ", TextType.NORMAL), TextNode("italic", TextType.ITALIC), TextNode(" wow!", TextType.NORMAL)])

    #def test_link(self):
    #    node = TextNode("This is text with a [link](http://example.com) word. omg two [link](http://example.com) wow!", TextType.NORMAL)
    #    
    #    self.assertEqual(split_nodes_delimiter([node], "[", TextType.LINK), [TextNode("This is text with a ", TextType.NORMAL), TextNode("link", TextType.LINK, "http://example.com"), TextNode(" word. omg two ", TextType.NORMAL), TextNode("link", TextType.LINK, "http://example.com"), TextNode(" wow!", TextType.NORMAL)])

    #def test_image(self):
    #    node = TextNode("This is text with a ![image](http://example.com) word. omg two ![image](http://example.com) wow!", TextType.NORMAL)
    #    self.assertEqual(split_nodes_delimiter([node], "![", TextType.IMAGE), [TextNode("This is text with a ", TextType.NORMAL), TextNode("image", TextType.IMAGE, "http://example.com"), TextNode(" word. omg two ", TextType.NORMAL), TextNode("image", TextType.IMAGE, "http://example.com"), TextNode(" wow!", TextType.NORMAL)])

    def test_no_delimiter(self):
        node = TextNode("This is text with a code block word. omg two code blocks wow!", TextType.NORMAL)
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), [node])

    def test_regex_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])

    def test_regex_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_url(text), [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')])

    def test_regex_link_missing_url(self):
        text = "This is text with a link [to boot dev]() and [to youtube]()"
        self.assertEqual(extract_markdown_url(text), [('to boot dev', ''), ('to youtube', '')])

    def test_regex_image_no_url(self):
        text = "This is text with a ![rick roll]() and ![obi wan]()"
        self.assertEqual(extract_markdown_images(text), [('rick roll', ''), ('obi wan', '')])

    def test_regex_link_missing_ref(self):
        text = "This is text with a link [](https://www.boot.dev) and [](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_url(text), [('', 'https://www.boot.dev'), ('', 'https://www.youtube.com/@bootdotdev')])

    def test_regex_image_no_ref(self):
        text = "This is text with a ![](https://i.imgur.com/aKaOqIh.gif) and ![](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [('', 'https://i.imgur.com/aKaOqIh.gif'), ('', 'https://i.imgur.com/fJRm4Vk.jpeg')])

    def test_split_nodes_url(self):
        node = []
        node.append(TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL))
        nodes = [
                    TextNode("This is text with a link ", TextType.NORMAL),
                    TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                    TextNode(" and ", TextType.NORMAL),
                    TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                ]
        self.assertEqual(split_nodes_url(node), nodes)
    
    def test_split_nodes_url_missing_ref(self):
        node = []
        node.append(TextNode("This is text with a link [](https://www.boot.dev) and [](https://www.youtube.com/@bootdotdev)", TextType.NORMAL))
        nodes = [
                    TextNode("This is text with a link ", TextType.NORMAL),
                    TextNode("", TextType.LINK, "https://www.boot.dev"),
                    TextNode(" and ", TextType.NORMAL),
                    TextNode("", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                ]
        self.assertEqual(split_nodes_url(node), nodes)
    def test_split_nodes_url_missing_url(self):
        node = []
        node.append(TextNode("This is text with a link [to boot dev]() and [to youtube]()", TextType.NORMAL))
        nodes = [
                    TextNode("This is text with a link ", TextType.NORMAL),
                    TextNode("to boot dev", TextType.LINK, None),
                    TextNode(" and ", TextType.NORMAL),
                    TextNode("to youtube", TextType.LINK, None),
                ]
        self.assertEqual(split_nodes_url(node), nodes)

    def test_split_nodes_url_no_url(self):
        node = []
        node.append(TextNode("This is text with a link to absolutely noting!", TextType.NORMAL))
        nodes = [
                    TextNode("This is text with a link to absolutely noting!", TextType.NORMAL),
                ]
        self.assertEqual(split_nodes_url(node), nodes)

    def test_split_nodes_image(self):
        node = []
        node.append(TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.NORMAL))
        nodes = [
                    TextNode("This is text with a ", TextType.NORMAL),
                    TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                    TextNode(" and ", TextType.NORMAL),
                    TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                ]
        self.assertEqual(split_nodes_image(node), nodes)

    def test_split_nodes_image_missing_ref(self):
        node = []
        node.append(TextNode("This is text with a ![](https://i.imgur.com/aKaOqIh.gif) and ![](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.NORMAL))
        nodes = [
                    TextNode("This is text with a ", TextType.NORMAL),
                    TextNode("", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                    TextNode(" and ", TextType.NORMAL),
                    TextNode("", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                ]
        self.assertEqual(split_nodes_image(node), nodes)
    
    def test_split_nodes_image_missing_url(self):
        node = []
        node.append(TextNode("This is text with a ![rick roll]() and ![obi wan]()", TextType.NORMAL))
        nodes = [
                    TextNode("This is text with a ", TextType.NORMAL),
                    TextNode("rick roll", TextType.IMAGE, None),
                    TextNode(" and ", TextType.NORMAL),
                    TextNode("obi wan", TextType.IMAGE, None),
                ]
        self.assertEqual(split_nodes_image(node), nodes)

    def test_split_image_no_links(self):
        node = []
        node.append(TextNode("This is text without any image references.", TextType.NORMAL))
        nodes = [
                    TextNode("This is text without any image references.", TextType.NORMAL),
                ]
        self.assertEqual(split_nodes_image(node), nodes)

    def test_text_to_textnode(self):
        text = "This is **text** with an *italic* word and a ```code block``` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        self.maxDiff = None
        self.assertEqual(text_to_textnodes(text), result)

    def test_markdown_to_blocks(self):
        text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n\n* This is a list item\n\n* This is another list item"
        result = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertEqual(markdown_to_blocks(text), result)

        text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n## THIS IS A NEW BLOCK\n\n### AND A NEW BLOCK\n\n* This is the first list item in a list block\n\n* This is a list item\n\n* This is another list item"
        result = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '## THIS IS A NEW BLOCK', '### AND A NEW BLOCK', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertEqual(markdown_to_blocks(text), result)

        text = "# BLOCK ONE\n\n## BLOCK TWO\n\n* BULLET ONE\n\n* BULLET TWO\n\nRANDOM TEXT\n\nRANDOM TEXT\n\n* RANDOM BULLET\n\n# RANDOM BLOCK"
        result = ['# BLOCK ONE', '## BLOCK TWO', '* BULLET ONE\n* BULLET TWO', 'RANDOM TEXT', 'RANDOM TEXT', '* RANDOM BULLET', '# RANDOM BLOCK']
        self.assertEqual(markdown_to_blocks(text), result)

        text = "# WOW A HEADER\n\n1. ORDERED LIST 1\n\n2. ORDERED LIST 2\n\n3. ORDERED LIST 3\n\n* UNORDERED SNEAKY\n\n* MORE UNORDERED\n\n# MASSIVE HEADER\n\n## MORE HEADER"
        result = ['# WOW A HEADER', '1. ORDERED LIST 1\n2. ORDERED LIST 2\n3. ORDERED LIST 3', '* UNORDERED SNEAKY\n* MORE UNORDERED', '# MASSIVE HEADER', '## MORE HEADER']
        self.assertEqual(markdown_to_blocks(text), result)
        
        text = "# This is a header\n\n`this is a code block`\n\nThis is a paragraph\n\n* This is an unordered list"
        result = ['# This is a header', '`this is a code block`', 'This is a paragraph', '* This is an unordered list']
        self.assertEqual(markdown_to_blocks(text), result)