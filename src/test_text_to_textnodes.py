import unittest
from split import *
from split_image_link import *
from textnode import *
from extract import *
from text_to_textnodes import *

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_text_nodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
        ],
        new_nodes
        )
    
    def test_text_to_text_nodes_empty(self):
        text = ""
        new_nodes = text_to_textnodes(text)
        self.assertEqual(new_nodes, [])

    def test_text_to_text_nodes_invalid(self):
        text = "This is **invalid markdown"
        with self.assertRaises(Exception):
            text_to_textnodes(text)
    
    def test_text_to_text_nodes_delimiter_only(self):
        text = "****"
        new_nodes = text_to_textnodes(text)
        self.assertEqual(new_nodes, [])

    def test_text_to_text_nodes_delimiter_space(self):
        text = "** **"
        new_nodes = text_to_textnodes(text)
        self.assertEqual(new_nodes, [TextNode(" ", TextType.BOLD)])
            