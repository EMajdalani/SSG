from md_to_htmlnode import *
from extract_title import *
import os
import shutil

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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    template_file = open(template_path, "r").read()
    content_dir_list = os.listdir(dir_path_content)

    for item in content_dir_list:
        item_path = os.path.join(dir_path_content, item)
        if os.path.isfile(item_path):
            md_file = open(item_path, "r").read()
            
            html_node = markdown_to_html_node(md_file)
            html_string = html_node.to_html()
            title_string = extract_title(md_file)

            index_title = template_file.replace("{{ Title }}", title_string)
            index_html = index_title.replace("{{ Content }}", html_string)
            strip_ext = item.rstrip(".md")
            new_filename = strip_ext + ".html"
            write_path = os.path.join(dest_dir_path, new_filename)

            with open(write_path, "w") as file:
                file.write(index_html)
            
        elif os.path.isdir(item_path):
            new_dir_path_content = item_path
            new_dest_dir_path = os.path.join(dest_dir_path, item)
            os.mkdir(new_dest_dir_path)
            generate_pages_recursive(new_dir_path_content, template_path, new_dest_dir_path)
        
    return
        











