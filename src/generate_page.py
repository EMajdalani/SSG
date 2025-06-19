from md_to_htmlnode import *
from extract_title import *
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md_file = open(from_path,"r").read()
    template_file = open(template_path, "r").read()

    html_node = markdown_to_html_node(md_file)
    html_string = html_node.to_html()
    title_string = extract_title(md_file)

    index_title = template_file.replace("{{ Title }}", title_string)
    index_html = index_title.replace("{{ Content }}", html_string)

    with open(dest_path, "w") as file:
        file.write(index_html)
    
    return










