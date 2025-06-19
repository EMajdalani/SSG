from split_blocks import *
from blocktype import *
from text_to_textnodes import *
from converters import *
from htmlnode import *

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

def block_to_paragraph(block):
    text = block.replace("\n", " ")
    children = text_to_children(text)
    return ParentNode("p", children)

def block_to_quote(block):
    quote_lines = block.split("\n")
    new_lines = []
    for line in quote_lines:
        new_line = line.lstrip("> ")
        new_lines.append(new_line)
    new_block = "\n".join(new_lines)
    children = text_to_children(new_block)
    return ParentNode("blockquote", children)

def block_to_code(block):
    text = block[block.index("\n") + 1 :block.rindex("```")]
    code_leaf_node = LeafNode(tag= None, value= text)
    child = ParentNode("code", [code_leaf_node])
    return ParentNode("pre", [child])

def uno_list_items(block):
    list_items = []

    list_lines = block.split("\n")
    list_marker = ("- ", "+ ", "* ")
    for line in list_lines:
        if line.startswith(list_marker):
            item = line.lstrip("-+* ")
            children = text_to_children(item)
            node = ParentNode("li", children)
            list_items.append(node)
    
    return list_items

def block_to_unordered_list(block):
    children = uno_list_items(block)
    return ParentNode("ul", children)

def ord_list_items(block):
    list_items = []
    line_count = 1

    list_lines = block.split("\n")
    for line in list_lines:
        list_marker = f"{line_count}. "
        if line.startswith(list_marker):
            item = line.lstrip(list_marker)
            children = text_to_children(item)
            node = ParentNode("li", children)
            list_items.append(node)
            line_count += 1
    
    return list_items

def block_to_ordered_list(block):
    children = ord_list_items(block)
    return ParentNode("ol", children)


def block_to_heading(block):
    hash_count = 0
    for char in block[:7]:
        if char == "#":
            hash_count += 1

    if hash_count > 6:
        return block_to_paragraph(block)

    elif len(block) >= hash_count +1 and block[hash_count] == " ":
        item = block.lstrip("# ")
        children = text_to_children(item)
        return ParentNode(f"h{hash_count}", children)
    
    else:
        return block_to_paragraph(block)


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            child = block_to_heading(block)
            children.append(child)
        
        if block_type == BlockType.PARAGRAPH:
            child = block_to_paragraph(block)
            children.append(child)
        
        if block_type == BlockType.CODE:
            child = block_to_code(block)
            children.append(child)
        
        if block_type == BlockType.QUOTE:
            child = block_to_quote(block)
            children.append(child)
        
        if block_type == BlockType.ORDLIST:
            child = block_to_ordered_list(block)
            children.append(child)
        
        if block_type == BlockType.UNOLIST:
            child = block_to_unordered_list(block)
            children.append(child)
    
    return ParentNode("div", children)



