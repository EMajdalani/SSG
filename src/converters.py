from textnode import TextType, TextNode
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if not isinstance(text_node.text_type, TextType):
        raise Exception ("Invalid text type")
    
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(tag=None, value=text_node.text)
    
    if text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    
    if text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    
    if text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    
    if text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("No url found")
        return LeafNode(tag="a", value=text_node.text, props={"href" : text_node.url})
    
    if text_node.text_type == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("No url found")
        return LeafNode(tag="img", value="", props={"src" : text_node.url, "alt" : text_node.text})