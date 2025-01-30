
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented
    
    def props_to_html(self):
        if self.props is None:
            return ""
        result = []
        #print(f"Props dictionary: {self.props}")
        for key, value in self.props.items():
            result.append(f'{key}="{value}"')
        return " " + " ".join(result)
    
    def __repr__(self):
        print(self.tag, self.value, self.children, self.props)