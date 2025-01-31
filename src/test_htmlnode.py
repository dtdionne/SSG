import unittest
from htmlnode import HTMLNode,LeafNode

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

if __name__ == "__main__":
    unittest.main()