import unittest
from htmlnode import *
from textnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_no_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_with_href(self):
        node = HTMLNode(props={"href": "https://bootdev.com"})
        self.assertEqual(node.props_to_html(), ' href="https://bootdev.com"')
    
    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={
            "href": "https://bootdev.com",
            "target": "_blank"
        })
        # This test is trickier because dict order isn't guaranteed
        result = node.props_to_html()
        self.assertTrue(' href="https://bootdev.com"' in result)
        self.assertTrue(' target="_blank"' in result)
        self.assertTrue(result.startswith(" "))

    def test_leafs(self):
        node1 = LeafNode("p", "Hello")
        self.assertEqual(node1.to_html(), "<p>Hello</p>")

        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node2.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

        node3 = LeafNode(None, "Just text")
        self.assertEqual(node3.to_html(), "Just text")

        with self.assertRaises(ValueError):
            node4 = LeafNode("p", None)
            node4.to_html()
 
    def test_text_node_to_html_node(self):
        # Test TEXT type
        node1 = TextNode("Hello, world!", TextType.TEXT)
        html_node1 = text_node_to_html_node(node1)
        self.assertEqual(html_node1.tag, None)
        self.assertEqual(html_node1.value, "Hello, world!")
        self.assertEqual(html_node1.props, None)

        # Test BOLD type
        node2 = TextNode("Bold text", TextType.BOLD)
        html_node2 = text_node_to_html_node(node2)
        self.assertEqual(html_node2.tag, "b")
        self.assertEqual(html_node2.value, "Bold text")
        self.assertEqual(html_node2.props, None)

        # Test LINK type
        node3 = TextNode("Click me", TextType.LINK, "https://boot.dev")
        html_node3 = text_node_to_html_node(node3)
        self.assertEqual(html_node3.tag, "a")
        self.assertEqual(html_node3.value, "Click me")
        self.assertEqual(html_node3.props, {"href": "https://boot.dev"})

        # Test invalid type
        with self.assertRaises(Exception):
            invalid_node = TextNode("test", "invalid_type")
            text_node_to_html_node(invalid_node)




if __name__ == "__main__":
    unittest.main()