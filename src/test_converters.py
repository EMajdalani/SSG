import unittest

from converters import *
from textnode import *
from htmlnode import *

class TestConverter(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")

    def test_italic(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")
    
    def test_code(self):
        node = TextNode("This text is code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This text is code")

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "www.google.com")
        node2 = TextNode("This is also a link", TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, {"href" : "www.google.com"})
        
        with self.assertRaises(ValueError):
            text_node_to_html_node(node2)
    
    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "www.image.com")
        node2 = TextNode("This is also an image", TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "www.image.com", "alt" : "This is an image"})

        with self.assertRaises(ValueError):
            text_node_to_html_node(node2)

    def test_value_error(self):
        node = TextNode("This should fail", "yes")
        node2 = TextNode("This should also fail", TextType.OTHER)

        with self.assertRaises(Exception):
            text_node_to_html_node(node)
        
        with self.assertRaises(ValueError):
            text_node_to_html_node(node2)


if __name__ == "__main__":
    unittest.main()