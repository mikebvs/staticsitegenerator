import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("div", "This is a text node", [], {"class": "test"})
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        node = HTMLNode("div", "This is a text node", [], {"class": "test", "id": "test"})
        self.assertEqual(node.props_to_html(), "class=\"test\" id=\"test\"")
    
    def test_props_to_html_empty(self):
        node = HTMLNode("div", "This is a text node", [], {})
        self.assertEqual(node.props_to_html(), "")

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_tag(self):
        node = LeafNode("p", "This is a paragraph of text.", None)
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_node_no_tag(self):
        node = LeafNode(None, "This is a paragraph of text.", None)
        self.assertEqual(node.to_html(), "This is a paragraph of text.")

    def test_leaf_node_props(self):
        node = LeafNode("p", "This is a paragraph of text.", {"class": "test"})
        self.assertEqual(node.to_html(), "<p class=\"test\">This is a paragraph of text.</p>")

    def test_leaf_node_no_value(self):
        node = LeafNode("p", None, None)
        self.assertRaises(ValueError, node.to_html)

class TestParentNode(unittest.TestCase):
    def test_parent_node(self):
        node = ParentNode("div", [LeafNode("p", "This is a paragraph of text.", None)], None)
        self.assertEqual(node.to_html(), "<div><p>This is a paragraph of text.</p></div>")
        

    def test_parent_nodes(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_multi_parent_tree(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                "div",
                    [
                        LeafNode("b", "Bolder text"),
                        LeafNode(None, "Normaler text"),
                        LeafNode("i", "italicer text"),
                        LeafNode(None, "Normaler text"),
                    ],
                )
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<div><b>Bolder text</b>Normaler text<i>italicer text</i>Normaler text</div></p>")

    def test_mid_nested_parent_tree(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                "div",
                    [
                        LeafNode("b", "Bolder text"),
                        LeafNode(None, "Normaler text"),
                        ParentNode(
                        "a",
                            [
                                LeafNode("b", "INNER Bolder text"),
                                LeafNode(None, "INNER Normaler text"),
                                LeafNode("i", "INNER italicer text"),
                                LeafNode(None, "INNER Normaler text"),
                            ],
                        ),
                        LeafNode("i", "italicer text"),
                        LeafNode(None, "Normaler text"),
                    ],
                )
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<div><b>Bolder text</b>Normaler text<a><b>INNER Bolder text</b>INNER Normaler text<i>INNER italicer text</i>INNER Normaler text</a><i>italicer text</i>Normaler text</div></p>")

    def test_no_children(self):
        node = ParentNode("p", [], None)
        self.assertRaises(ValueError, node.to_html)

    def test_no_tag(self):
        node = ParentNode(None, [LeafNode("b", "Bold text")], None)
        self.assertRaises(ValueError, node.to_html)

    def test_no_tag_no_children(self):
        node = ParentNode(None, [], None)
        self.assertRaises(ValueError, node.to_html)

if __name__ == "__main__":
    unittest.main()