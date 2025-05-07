import unittest

from textnode import *
from split import *

class TestSplit(unittest.TestCase):
    def test_split_text(self):
        node = [TextNode("This is normal text", TextType.TEXT)]
        split_node = split_nodes_delimiter(node, "**", TextType.BOLD)
        self.assertEqual(split_node, [
            TextNode("This is normal text", TextType.TEXT)
        ])
    
    def test_split_bold(self):
        node = [TextNode("This is **bold** text", TextType.TEXT)]
        split_node = split_nodes_delimiter(node, "**", TextType.BOLD)
        self.assertEqual(split_node, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ])

    def test_split_italic(self):
        node = [TextNode("This is _italic_ text", TextType.TEXT)]
        split_node = split_nodes_delimiter(node, "_", TextType.ITALIC)
        self.assertEqual(split_node, [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ])
    
    def test_split_code(self):
        node = [TextNode("This is ```code``` text", TextType.TEXT)]
        split_node = split_nodes_delimiter(node, "```", TextType.CODE)
        self.assertEqual(split_node, [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT)
        ])
    
    def test_split_exception(self):
        node = [TextNode("This is **invalid markdown", TextType.TEXT)]
        with self.assertRaises(Exception):
            split_nodes_delimiter(node, "**", TextType.BOLD)

    def test_split_image(self):
        node1 = [TextNode("This is an image", TextType.IMAGE, "www.image.com")]
        split_node = split_nodes_delimiter(node1, "**", TextType.BOLD)
        self.assertEqual(split_node, [
            TextNode("This is an image", TextType.IMAGE, "www.image.com")
        ])
    
    def test_split_link(self):
        node1 = [TextNode("This is a link", TextType.LINK, "www.link.com")]
        split_node = split_nodes_delimiter(node1, "**", TextType.BOLD)
        self.assertEqual(split_node, [
            TextNode("This is a link", TextType.LINK, "www.link.com")
        ])

    