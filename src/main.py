import sys
import shutil
import os
from generate_page import *

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    static_path = "static"
    doc_path = "docs"
    from_path = "content"
    template_path = "template.html"
    dest_path = "docs"
    
    copy_static(static_path, doc_path)
    generate_pages_recursive(from_path, template_path, dest_path, basepath)


def copy_recursive(source_dir, dest_dir):
    source_dir_list = os.listdir(source_dir)
    for item in source_dir_list:
        item_path = os.path.join(source_dir, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, dest_dir)
        elif os.path.isdir(item_path):
            new_source_dir = item_path
            new_dest_dir = os.path.join(dest_dir, item)
            os.mkdir(new_dest_dir)
            copy_recursive(new_source_dir, new_dest_dir)
    
    return

def copy_static(source_dir, dest_dir):
    if os.path.isdir(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)
    copy_recursive(source_dir, dest_dir)
    
    return
        

main()