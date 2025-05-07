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

    def test_split_adjacent(self):
        node = [TextNode("This is **bold****and more bold** text", TextType.TEXT)]
        split_node = split_nodes_delimiter(node, "**", TextType.BOLD)
        self.assertEqual(split_node, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode("and more bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ])
    
    def test_split_start_end_delim(self):
        node = [TextNode("**bold** text this is **also bold**", TextType.TEXT)]
        split_node = split_nodes_delimiter(node, "**", TextType.BOLD)
        self.assertEqual(split_node, [
            TextNode("bold", TextType.BOLD),
            TextNode(" text this is ", TextType.TEXT),
            TextNode("also bold", TextType.BOLD)    
        ])
    
    def test_split_nested(self):
        node = [TextNode("This is **bold and ```coded```** text", TextType.TEXT)]
        split_node = split_nodes_delimiter(node, "**", TextType.BOLD)
        self.assertEqual(split_node, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold and ```coded```", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ])
    
    def test_split_multiple(self):
        node = [TextNode("This is **bold** _italic_ and ```coded``` in the same line", TextType.TEXT)]
        split_node = split_nodes_delimiter(node, "**", TextType.BOLD)
        self.assertEqual(split_node, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" _italic_ and ```coded``` in the same line", TextType.TEXT)
        ])
    
    def test_split_all(self):
        node = [TextNode("This is **bold** _italic_ and ```coded``` in the same line", TextType.TEXT)]
        split_node = split_nodes_delimiter(node, "**", TextType.BOLD)
        split_node = split_nodes_delimiter(split_node, "_", TextType.ITALIC)
        split_node = split_nodes_delimiter(split_node, "```", TextType.CODE)
        self.assertEqual(split_node, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("coded", TextType.CODE),
            TextNode(" in the same line", TextType.TEXT)
        ])
        
    def test_split_list(self):
        node = [
            TextNode("This is regular text", TextType.TEXT),
            TextNode("This is text with **bold** in it", TextType.TEXT),
            TextNode("This is text with _italic_ and ```code``` in it", TextType.TEXT),
            TextNode("This is an image", TextType.IMAGE, "wwww.image.com"),
            TextNode("This is a link", TextType.LINK, "www.link.com"),
            TextNode("This is already bold", TextType.BOLD),
            TextNode("This is **bold** _italic_ and ```coded``` in the same line", TextType.TEXT)
        ]
        split_node = split_nodes_delimiter(node, "**", TextType.BOLD)
        split_node = split_nodes_delimiter(split_node, "_", TextType.ITALIC)
        split_node = split_nodes_delimiter(split_node, "```", TextType.CODE)
        
        self.assertEqual(split_node, [
            TextNode("This is regular text", TextType.TEXT),
            TextNode("This is text with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" in it", TextType.TEXT),
            TextNode("This is text with ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" in it", TextType.TEXT),
            TextNode("This is an image", TextType.IMAGE, "wwww.image.com"),
            TextNode("This is a link", TextType.LINK, "www.link.com"),
            TextNode("This is already bold", TextType.BOLD),
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("coded", TextType.CODE),
            TextNode(" in the same line", TextType.TEXT)         
        ])
