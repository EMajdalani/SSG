from split import *
from split_image_link import *
from textnode import *
from extract import *

def text_to_textnodes(text):
    first_text_node = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(first_text_node, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes
        