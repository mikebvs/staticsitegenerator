import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        self.assertNotEqual(node, node2)

    def test_different_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_text_different(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        node2 = TextNode("This is another text node", TextType.BOLD, "http://example.com")
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.to_html(), "<b>This is a text node</b>")

    def test_text_node_to_html_node_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.to_html(), "<i>This is a text node</i>")
    
    def test_text_to_html_img(self):
        node = TextNode("", TextType.IMAGE, "http://example.com")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.to_html(), '<img src="http://example.com" alt="">')

    def test_text_to_html_img_with_value(self):
        node = TextNode("test value", TextType.IMAGE, "http://example.com")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.to_html(), '<img src="http://example.com" alt="test value">')

    def test_text_to_html_with_link(self):
        node = TextNode("test value", TextType.LINK, "http://example.com")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.to_html(), '<a href="http://example.com">test value</a>')

    #def test_text_to_html_invalid_type(self):
    #    node = TextNode("test value", "random", "http://example.com")
    #    self.assertRaises(AttributeError, node.text_node_to_html_node)

if __name__ == "__main__":
    unittest.main()