from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

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

### REGEX C3.4

import re

def extract_markdown_images(text):
    # Use the regex from the lesson to find image markdown patterns
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    
    # Return the matches
    return matches

# Simple test
if __name__ == "__main__":
    print("Testing extract_markdown_images...")
    markdown_text = "This is text with an image: ![test image](https://example.com/image.png)"
    print(extract_markdown_images(markdown_text))

def extract_markdown_links(text):
    # Your regex and logic here!
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

if __name__ == "__main__":
    print("Testing extract_markdown_links...")
    markdown_text = "This has a link [to Boot.dev](https://boot.dev) and [to Google](https://google.com)"
    print(extract_markdown_links(markdown_text))