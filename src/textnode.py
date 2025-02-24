from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL = "normal_text"
    BOLD = "bold_text"
    ITALIC = "italic_text"
    CODE = "code_text"
    LINK = "link_text"
    IMAGE = "image_text"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        if self.text_type not in TextType:
            raise AttributeError("Invalid TextType")

    def __repr__(self):
        return f"TextNode(\"{self.text}\", {self.text_type.value}, {self.url})"
    
    def __eq__(self, textnode):
        if (self.text == textnode.text and 
        self.text_type == textnode.text_type and 
        self.url == textnode.url):
            return True
        else:
            return False


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"invalid text type: {text_node.text_type}")
