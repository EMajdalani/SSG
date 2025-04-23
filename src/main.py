from enum import Enum
from textnode import *

def main():
    text = "this is some random text"
    url = "https://www.boot.dev"
    print   (TextNode(text, TextType("link") , url))


main()