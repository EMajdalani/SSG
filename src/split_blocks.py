def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    new_blocks = []
    for block in raw_blocks:
        new_block = block.strip()
        if new_block != "":
            new_blocks.append(new_block)
    return new_blocks