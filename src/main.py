from textnode import *

def block_to_block_type(block: str) -> str:
    if block.startswith('#'):
        words = block.split(' ')
        first_word = words[0]
        if 1 <= len(first_word) <= 6 and all(char == '#' for char in first_word):
            return "heading"
        
    if block.startswith('```') and block.endswith('```'):
        #words = block.split(' ')
        #first_word = words[0]
        #if 1 <= len(first_word) <= 6 and all(char == '#' for char in first_word):
        return "code"
    
    lines = [line for line in block.split('\n') if line.strip()]
    
    if all(line.startswith('>') for line in lines):
        return "quote"
    
    if all(line.startswith('* ') or line.startswith('- ') for line in lines):
        return "unordered_list"
    
    for i, line in enumerate(lines, start=1):
        if not line.startswith(f'{i}. '):
            break
    else:
        return "ordered_list"
    return "paragraph"

def main():
    #print("hello world")
    test_node = TextNode("dtd", TextType.BOLD)
    print(test_node)

main()
