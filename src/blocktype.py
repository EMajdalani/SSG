from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNOLIST = "unordered list"
    ORDLIST = "ordered list"

def block_to_block_type(block):
    headings = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    code = "```"
    if block.startswith(headings):
        return BlockType.HEADING
    
    if block.startswith(code) and block.endswith(code):
        return BlockType.CODE
    
    if block.startswith(">"):
        split_block = block.split('\n')
        for line in split_block:
            if line.startswith(">") == False:
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if block.startswith("- "):
        split_block = block.split('\n')
        for line in split_block:
            if line.startswith("- ") == False:
                return BlockType.PARAGRAPH
        return BlockType.UNOLIST
    
    if block.startswith("1. "):
        split_block = block.split('\n')
        num = 1
        for line in split_block:
            if line.startswith(f"{num}. ") == False:
                return BlockType.PARAGRAPH
            num += 1
        return BlockType.ORDLIST
    
    return BlockType.PARAGRAPH

            


    