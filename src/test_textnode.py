import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.LINK)
        node4 = TextNode("This is not a text node", TextType.BOLD)
        node5 = TextNode("This is a text node", TextType.NORMAL, "https://boot.dev")
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node4)
        self.assertTrue(node.url == None)
        self.assertTrue(node5.url != None)


if __name__ == "__main__":
    unittest.main()