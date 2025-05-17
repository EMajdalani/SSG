import unittest
from textnode import *
from split_image_link import *
from extract import *

class TestSplitImageLink(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes
        )
    
    def test_split_images_expanded(self):
        nodes = [
            TextNode("This is text without an image or link", TextType.TEXT),
            TextNode("This is bold text", TextType.BOLD),
            TextNode("![image](https://i.imgur.com/zjjcJKZ.png) This is text with images at the edges ![image2](https://i.imgur2.com/zjjcJKZ.png)", TextType.TEXT),
            TextNode("![image3](https://i.imgur3.com/zjjcJKZ.png)![image4](https://i.imgur4.com/zjjcJKZ.png)", TextType.TEXT),
            TextNode("This is text with a [link](https://link.com)", TextType.TEXT)
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertEqual(
            [
            TextNode("This is text without an image or link", TextType.TEXT),
            TextNode("This is bold text", TextType.BOLD),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" This is text with images at the edges ", TextType.TEXT),
            TextNode("image2", TextType.IMAGE, "https://i.imgur2.com/zjjcJKZ.png"),
            TextNode("image3", TextType.IMAGE, "https://i.imgur3.com/zjjcJKZ.png"),
            TextNode("image4", TextType.IMAGE, "https://i.imgur4.com/zjjcJKZ.png"),
            TextNode("This is text with a [link](https://link.com)", TextType.TEXT)
        ],
        new_nodes    
    )


    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://link.com) and another [second link](https://second_link.com)", TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://second_link.com") 
            ],
            new_nodes
        )
    
    def test_split_links_expanded(self):
        nodes = [
            TextNode("This is text without an image or link", TextType.TEXT),
            TextNode("This is bold text", TextType.BOLD),
            TextNode("[link](https://i.imgur.com/zjjcJKZ.png) This is text with links at the edges [link2](https://i.imgur2.com/zjjcJKZ.png)", TextType.TEXT),
            TextNode("[link3](https://i.imgur3.com/zjjcJKZ.png)[link4](https://i.imgur4.com/zjjcJKZ.png)", TextType.TEXT),
            TextNode("This is text with an ![image](https://image.com)", TextType.TEXT)
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertEqual(
            [
            TextNode("This is text without an image or link", TextType.TEXT),
            TextNode("This is bold text", TextType.BOLD),
            TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" This is text with links at the edges ", TextType.TEXT),
            TextNode("link2", TextType.LINK, "https://i.imgur2.com/zjjcJKZ.png"),
            TextNode("link3", TextType.LINK, "https://i.imgur3.com/zjjcJKZ.png"),
            TextNode("link4", TextType.LINK, "https://i.imgur4.com/zjjcJKZ.png"),
            TextNode("This is text with an ![image](https://image.com)", TextType.TEXT)
        ],
        new_nodes    
    )
