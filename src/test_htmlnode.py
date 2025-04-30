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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        empty_parent_one = ParentNode("a", [])
        empty_parent_two = ParentNode("b", None)
        empty_tag = ParentNode(None, [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        with self.assertRaises(ValueError):
            empty_parent_one.to_html()
        with self.assertRaises(ValueError):
            empty_parent_two.to_html()
        with self.assertRaises(ValueError):
            empty_tag.to_html()


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_family_tree(self):
        grandchild_node_one = LeafNode("p", "grandchild one")
        grandchild_node_two = LeafNode("gc", "grandchild two")
        grandchild_node_three = LeafNode("bb", "grandchild three")
        child_node_two = ParentNode("d", [grandchild_node_three])
        child_node_one = ParentNode("m", [grandchild_node_one, grandchild_node_two])
        parent_node = ParentNode("g", [child_node_one, child_node_two])
        self.assertEqual(
            parent_node.to_html(),
            "<g><m><p>grandchild one</p><gc>grandchild two</gc></m><d><bb>grandchild three</bb></d></g>"
        )
