import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("THIS is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://ssh3112.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_difurl(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://duckduckgo.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()