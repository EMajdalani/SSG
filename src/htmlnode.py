class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        props_string = ""
        for k, v in self.props.items():
            props_string += f' {k}="{v}"'
        return props_string
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        props_str = self.props_to_html()
        if self.value == None:
            raise ValueError ("Value must not be blank")
        if self.tag == None:
            return str(self.value)
        if props_str == "":
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"