from enum import Enum

class TextType(Enum):
    NORMAL_TEXTTYPE = "normal"
    BOLD_TEXTTYPE = "bold"
    ITALIC_TEXTTYPE = "italic"
    CODE_TEXTTYPE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
