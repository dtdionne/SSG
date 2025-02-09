from textnode import TextType, TextNode


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

