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
