from enum import Enum
#from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

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

def extract_markdown_links(text):
    # Your regex and logic here!
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, delimiter="**", text_type=TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, delimiter="*", text_type=TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, delimiter="`", text_type=TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

#SPLIT_NODES.PY

#from text_node import TextNode, TextType
#from textnode import TextNode, TextType

def markdown_to_blocks(markdown):
    return [block.strip() for block in re.split(r'\n\s*\n', markdown.strip())]


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    
    # Handle multiple nodes (case 3)
    for node in old_nodes:
        # Only try to split nodes that are text type
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
            
        text = node.text
        first_delimiter = text.find(delimiter)
        
        # No delimiter found (case 1)
        
        if first_delimiter == -1:
            result.append(node)
            continue
            
        second_delimiter = text.find(delimiter, first_delimiter + 1)
        # No closing delimiter (case 2)
        if second_delimiter == -1:
            raise ValueError("No closing delimiter found")
            
        before_node = TextNode(text[0:first_delimiter], TextType.TEXT)
        code_node = TextNode(text[first_delimiter + 1:second_delimiter], text_type)
        after_node = TextNode(text[second_delimiter + 1:], TextType.TEXT)
        
        result.extend([before_node, code_node, after_node])
    
    return result

def split_nodes_image(old_nodes):
    result  = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
                result.append(node)
                continue
        images = extract_markdown_images(node.text)
        if not images:
            result.append(node)
            continue
        for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            sections = node.text.split(image_markdown, 1)
            if sections[0]:
                result.append(TextNode(sections[0], TextType.TEXT))
            result.append(TextNode(alt_text, TextType.IMAGE, url))
            if sections[1]:
                result.append(TextNode(sections[1], TextType.TEXT))
    return result


def split_nodes_link(old_nodes):
    result  = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
                result.append(node)
                continue
        links = extract_markdown_links(node.text)
        if not links:
            result.append(node)
            continue
        for alt_text, url in links:
            link_markdown = f"[{alt_text}]({url})"
            sections = node.text.split(link_markdown, 1)
            if sections[0]:
                result.append(TextNode(sections[0], TextType.TEXT))
            result.append(TextNode(alt_text, TextType.LINK, url))
            if sections[1]:
                result.append(TextNode(sections[1], TextType.TEXT))
    return result


if __name__ == "__main__":
    # Create a mixed list of nodes
    nodes = [
        TextNode("Here's some text with `code` in it", TextType.TEXT),
        TextNode("This is bold", TextType.BOLD),
        TextNode("And some text with another `code block`", TextType.TEXT)
    ]
    
    # Try splitting them
    result = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    # Print each node to see what happened
    for node in result:
        print(f"Text: '{node.text}', Type: {node.text_type}")

if __name__ == "__main__":
    test_cases = [
        TextNode("Install it with `npm install`", TextType.TEXT),
        TextNode("The command `ls -la` lists all files", TextType.TEXT),
        TextNode("Type `exit` to quit the program", TextType.TEXT),
        TextNode("To save, press `ctrl+s` and to quit press `cmd+q`", TextType.TEXT)
    ]
    
    print("Testing realistic Markdown examples:")
    print("-" * 40)
    
    for test_node in test_cases:
        print(f"\nOriginal: {test_node.text}")
        result = split_nodes_delimiter([test_node], "`", TextType.CODE)
        print("Splits into:")
        for node in result:
            print(f"- '{node.text}' ({node.text_type})")

#SPLIT_NODES.PY






#def test_text_to_textnodes():
if __name__ == "__main__":
    text = "This is **bold** text with *italic* and `code`"
    testnodes = text_to_textnodes(text)
    # You can print the nodes to see what you're getting
    for node in testnodes:
        print(f"Text: {node.text}, Type: {node.text_type}")

# Simple test
if __name__ == "__main__":
    print("Testing extract_markdown_images...")
    markdown_text = "This is text with an image: ![test image](https://example.com/image.png)"
    print(extract_markdown_images(markdown_text))

if __name__ == "__main__":
    print("Testing extract_markdown_links...")
    markdown_text = "This has a link [to Boot.dev](https://boot.dev) and [to Google](https://google.com)"
    print(extract_markdown_links(markdown_text))

def test_markdown_to_blocks():
    # Test case 1: Basic blocks
    markdown = """This is paragraph 1.

This is paragraph 2."""
    expected = [
        "This is paragraph 1.",
        "This is paragraph 2."
    ]
    assert markdown_to_blocks(markdown) == expected

    # Test case 2: Multiple blank lines between blocks
    markdown = """This is paragraph 1.


This is paragraph 2."""
    expected = [
        "This is paragraph 1.",
        "This is paragraph 2."
    ]
    assert markdown_to_blocks(markdown) == expected

    # Test case 3: Lists and headings
    markdown = """# Header

* List item 1
* List item 2

Final paragraph."""
    expected = [
        "# Header",
        "* List item 1\n* List item 2",
        "Final paragraph."
    ]
    assert markdown_to_blocks(markdown) == expected

    print("All markdown_to_blocks tests passed!")

if __name__ == "__main__":
    test_markdown_to_blocks()