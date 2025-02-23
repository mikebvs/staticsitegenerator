

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        def deconstruct_html(prop):
            return f"{prop[0]}=\"{prop[1]}\""
        props = list(map(deconstruct_html, self.props.items()))
        return " ".join(props)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        
        if self.tag == None:
            return (f"{self.value}")
        elif self.props:
            if self.tag == "img":
                return f"<{self.tag} {self.props_to_html()}>"
            else:
                return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag must be provided for ParentNode")
        if not self.children:
            raise ValueError("Children must be provided for ParentNode")
        concat_string = f"<{self.tag}>"
        for child in self.children:
            concat_string += child.to_html()
        return (f"{concat_string}</{self.tag}>")

        
        
