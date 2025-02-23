import unittest

from textnode import TextNode, TextType
from blocktype import BlockType, block_to_block_type


class TestBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        block = "# Header 1"
        result = BlockType.HEADING
        self.assertEqual(block_to_block_type(block), result)

        block = "## Header 2"
        result = BlockType.HEADING
        self.assertEqual(block_to_block_type(block), result)

        block = "### Header 3"
        result = BlockType.HEADING
        self.assertEqual(block_to_block_type(block), result)

        block = "#### Header 4"
        result = BlockType.HEADING
        self.assertEqual(block_to_block_type(block), result)

        block = "##### Header 5"
        result = BlockType.HEADING
        self.assertEqual(block_to_block_type(block), result)

        block = "###### Header 6"
        result = BlockType.HEADING
        self.assertEqual(block_to_block_type(block), result)

        block = "* Unordered List 1"
        result = BlockType.UNORDERED_LIST
        self.assertEqual(block_to_block_type(block), result)

        block = "- Unordered List 2"
        result = BlockType.UNORDERED_LIST
        self.assertEqual(block_to_block_type(block), result)

        block = "1. Ordered List 1"
        result = BlockType.ORDERED_LIST
        self.assertEqual(block_to_block_type(block), result)

        block = "1. Ordered List 1\n2. Ordered List 2\n3. Ordered List 3"
        result = BlockType.ORDERED_LIST
        self.assertEqual(block_to_block_type(block), result)

        block = "16. Ordered List 16"
        result = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(block), result)

        block = "```\nCode Block 1\n```"
        result = BlockType.CODE
        self.assertEqual(block_to_block_type(block), result)

        block = "```Code Block 2```"
        result = BlockType.CODE
        self.assertEqual(block_to_block_type(block), result)
    
        block = "`Code Snippet 1`"
        result = BlockType.CODE
        self.assertEqual(block_to_block_type(block), result)

