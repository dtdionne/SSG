import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()