import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode()
        node2 = HTMLNode("h1")
        node3 = HTMLNode("a", "text", None, {"href": "https://www.google.com"})
        node4 = HTMLNode("a", "b", None, {
        "href": "https://www.google.com",
        "target": "_blank" })
        test_case1 = ' href="https://www.google.com" target="_blank"'
        test_case2 = ""
        test_case3 = ' href="https://www.google.com"'
        self.assertEqual(node4.props_to_html(), test_case1)
        self.assertEqual(node.props_to_html(), test_case2)
        self.assertEqual(node3.props_to_html(), test_case3)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node3 = LeafNode(None, "Hello world!")
        node4 = LeafNode("d", None)
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
        self.assertEqual(node3.to_html(), "Hello world!")
        with self.assertRaises(ValueError):
            node4.to_html()