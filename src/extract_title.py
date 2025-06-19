def extract_title(markdown):
    md_split = markdown.split("\n")
    header = md_split[0]
    if header[0] == "#" and header[1] == " ":
        title = header.strip("# ")
        return title
    else:
        raise Exception ("No header found")