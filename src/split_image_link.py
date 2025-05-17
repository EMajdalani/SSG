from textnode import *
from extract import *

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            text = node.text

            while extract_markdown_images(text) !=[]:
                image_alt, image_link = extract_markdown_images(text)[0]
                sections = text.split(f"![{image_alt}]({image_link})", 1)
                
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                text = sections[1]
            
            if text != "":
                new_nodes.append(TextNode(text, TextType.TEXT))
        
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            text = node.text

            while extract_markdown_links(text) !=[]:
                alt_text, link = extract_markdown_links(text)[0]
                sections = text.split(f"[{alt_text}]({link})", 1)
                
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(alt_text, TextType.LINK, link))
                text = sections[1]
            
            if text != "":
                new_nodes.append(TextNode(text, TextType.TEXT))
        
        else:
            new_nodes.append(node)
    return new_nodes