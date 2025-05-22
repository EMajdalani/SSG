import unittest
from blocktype import *

class TestBlockType(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        heading_one = "# This is a heading"
        heading_two = "## This is a heading"
        heading_three = "### This is a heading"
        heading_four = "#### This is a heading"
        heading_five = "##### This is a heading"
        heading_six = "###### This is a heading"
        heading_seven = "#This is a paragraph"

        self.assertEqual(block_to_block_type(heading_one), BlockType.HEADING)
        self.assertEqual(block_to_block_type(heading_two), BlockType.HEADING)
        self.assertEqual(block_to_block_type(heading_three), BlockType.HEADING)
        self.assertEqual(block_to_block_type(heading_four), BlockType.HEADING)
        self.assertEqual(block_to_block_type(heading_five), BlockType.HEADING)
        self.assertEqual(block_to_block_type(heading_six), BlockType.HEADING)
        self.assertEqual(block_to_block_type(heading_seven), BlockType.PARAGRAPH)

    def test_block_to_block_type_code(self):
        code_one = "```This is a code```"
        code_two = "```This is a paragraph`"
        code_three = "`This is a paragraph"

        self.assertEqual(block_to_block_type(code_one), BlockType.CODE)
        self.assertEqual(block_to_block_type(code_two), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(code_three), BlockType.PARAGRAPH)

    def test_block_to_block_type_quote(self):
        quote_one = ">This is a quote"
        quote_two = "> This is also a quote"
        quote_three = ">This is a\n>split quote"
        quote_four = "> This is also a\n> split quote"
        quote_five = ">This is a\n paragraph"
        quote_six = "This is also a\n> a paragraph"
        
        self.assertEqual(block_to_block_type(quote_one), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(quote_two), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(quote_three), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(quote_four), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(quote_five), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(quote_six), BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list(self):
        list_one = "- list item one\n- list item two\n- list item three"
        list_two = "- list item one"
        list_three = "- list item one\n-oops paragraph\n- list item two"
        list_four = "-list item one"
        list_five = "- list item one\n- \n- list item two"
        list_six = "- list item one\n-\n- list item two" 
        
        self.assertEqual(block_to_block_type(list_one), BlockType.UNOLIST)
        self.assertEqual(block_to_block_type(list_two), BlockType.UNOLIST)
        self.assertEqual(block_to_block_type(list_three), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(list_four), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(list_five), BlockType.UNOLIST)
        self.assertEqual(block_to_block_type(list_six), BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list(self):
        list_one = "1. This is a list"
        list_two = "1. List item one\n2. List item two"
        list_three = "2. List item two"
        list_four = "1.List item one"
        list_five = "1. List item one\n3. List item two"
        list_six = "1. List item one\n2.List item two"

        self.assertEqual(block_to_block_type(list_one), BlockType.ORDLIST)
        self.assertEqual(block_to_block_type(list_two), BlockType.ORDLIST)
        self.assertEqual(block_to_block_type(list_three), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(list_four), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(list_five), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(list_six), BlockType.PARAGRAPH)