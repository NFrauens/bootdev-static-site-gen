import unittest
from blocktype import BlockType, block_to_block_type

class test_block_to_blocktype(unittest.TestCase):
    def test_heading(self):
        block = block_to_block_type("###### TITLE BLOCK")
        self.assertEqual(block, BlockType.HEADING)

    def test_codeblock(self):
        block = block_to_block_type("```\nthis is a code block\n```")
        self.assertEqual(block, BlockType.CODE)

    def test_quoteblock(self):
        block = block_to_block_type(">john quoteme\n>this is a great quote\n>perhaps the greatest of all.")
        self.assertEqual(block, BlockType.QUOTE)

    def test_unorderedlistgood(self):
        block = block_to_block_type("- this\n- is\n- a\n- list")
        self.assertEqual(block, BlockType.UNORDERED_LIST)

    def test_unorderedlistbad(self):
        block = block_to_block_type("-this\n-is\n-a\nbad\n-list")
        self.assertEqual(block, BlockType.PARAGRAPH)

    def test_orderedlistgood(self):
        block = block_to_block_type("1. this\n2. is\n3. a\n4. list")
        self.assertEqual(block, BlockType.ORDERED_LIST)

    def test_orderedlistbad(self):
        block = block_to_block_type("1.this\n2.is\n3.a\n4.bad\n5.list")
        self.assertEqual(block, BlockType.PARAGRAPH)

    def test_orderedlistbad2(self):
        block = block_to_block_type("1. this\n3. is\n5. list")
        self.assertEqual(block, BlockType.PARAGRAPH)