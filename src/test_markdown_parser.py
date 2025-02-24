import unittest

from textnode import TextNode, TextType
from parsemarkdown import *
from markdown_parser import markdown_to_html_node, extract_title
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestMarkdownParser(unittest.TestCase):
    def test_markdown(self):
        pass
    #def test_markdown_to_html_node(self):
    #    markdown = "# h1 Heading\n\n## h2 Heading with **bold** text!\n\n### h3 Heading\n\n#### h4 Heading\n\n##### h5 Heading\n\n###### h6 Heading\n\nParagraph Text with *italics* as well as some **bold** text!\n\n'this is a paragraph with a [link](https://www.google.com) in it!\n\n* Unordered List\n\n* Unordered List Again\n\n- Another Unordered List Format\n\n1. Ordered List 1\n\n2. Ordered List 2\n\n```\nThis is a fenced code block\n```\n\na paragraph\nwith a new line\n\na paragraph with ![an image](https://imageurl.com)\n\nand a very cool `Code Block` wow check that out\n\n> Block Quote\n> Many Lines\n> Very important quote"
    #    result = "[HTMLNode(h1, None, [LeafNode(None, h1 Heading, None)], None), HTMLNode(h2, None, [LeafNode(None, h2 Heading with , None), LeafNode(b, bold, None), LeafNode(None,  text!, None)], None), HTMLNode(h3, None, [LeafNode(None, h3 Heading, None)], None), HTMLNode(h4, None, [LeafNode(None, h4 Heading, None)], None), HTMLNode(h5, None, [LeafNode(None, h5 Heading, None)], None), HTMLNode(h6, None, [LeafNode(None, h6 Heading, None)], None), HTMLNode(p, None, [[LeafNode(None, Paragraph Text with , None), LeafNode(i, italics, None), LeafNode(None,  as well as some , None), LeafNode(b, bold, None), LeafNode(None,  text!, None)]], None), HTMLNode(p, None, [[LeafNode(None, 'this is a paragraph with a , None), LeafNode(a, link, {'href': 'https://www.google.com'}), LeafNode(None,  in it!, None)]], None), HTMLNode(ul, None, [HTMLNode(li, None, [LeafNode(None, Unordered List, None)], None), HTMLNode(li, None, [LeafNode(None, Unordered List Again, None)], None)], None), HTMLNode(ul, None, [HTMLNode(li, None, [LeafNode(None, Another Unordered List Format, None)], None)], None), HTMLNode(ol, None, [HTMLNode(li, None, [LeafNode(None, Ordered List 1, None)], None), HTMLNode(li, None, [LeafNode(None, Ordered List 2, None)], None)], None), HTMLNode(pre, None, [LeafNode(code, This is a fenced code block, None)], None), HTMLNode(p, None, [[LeafNode(None, a paragraph, None), LeafNode(None, with a new line, None)]], None), HTMLNode(p, None, [[LeafNode(None, a paragraph with , None), LeafNode(img, , {'src': 'https://imageurl.com', 'alt': 'an image'})]], None), HTMLNode(p, None, [[LeafNode(None, and a very cool , None), LeafNode(code, Code Block, None), LeafNode(None,  wow check that out, None)]], None), HTMLNode(blockquote, None, [HTMLNode(p, None, [LeafNode(None, Block Quote, None), LeafNode(None, Many Lines, None), LeafNode(None, Very important quote, None)], None)], None)]"
    #    self.maxDiff = None
    #    self.assertEqual(markdown_to_html_node(markdown), result)

    def test_extract_title(self):
        markdown = "# h1 Heading\n\n## h2 Heading with **bold** text!\n\n### h3 Heading\n\n#### h4 Heading\n\n##### h5 Heading\n\n###### h6 Heading\n\nParagraph Text with *italics* as well as some **bold** text!\n\n'this is a paragraph with a [link](https://www.google.com) in it!\n\n* Unordered List\n\n* Unordered List Again\n\n- Another Unordered List Format\n\n1. Ordered List 1\n\n2. Ordered List 2\n\n```\nThis is a fenced code block\n```\n\na paragraph\nwith a new line\n\na paragraph with ![an image](https://imageurl.com)\n\nand a very cool `Code Block` wow check that out\n\n> Block Quote\n> Many Lines\n> Very important quote"
        result = "h1 Heading"
        self.assertEqual(extract_title(markdown), result)

        markdown = "## h2 Heading\n\n## h2 Heading with **bold** text!\n\n### h3 Heading\n\n#### h4 Heading\n\n##### h5 Heading\n\n###### h6 Heading\n\nParagraph Text with *italics* as well as some **bold** text!\n\n'this is a paragraph with a [link](https://www.google.com) in it!\n\n* Unordered List\n\n* Unordered List Again\n\n- Another Unordered List Format\n\n1. Ordered List 1\n\n2. Ordered List 2\n\n```\nThis is a fenced code block\n```\n\na paragraph\nwith a new line\n\na paragraph with ![an image](https://imageurl.com)\n\nand a very cool `Code Block` wow check that out\n\n> Block Quote\n> Many Lines\n> Very important quote"
        result = Exception
        self.assertRaises(result, extract_title)
