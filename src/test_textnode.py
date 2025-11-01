import unittest

from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node without a url", TextType.TEXT)
        self.assertIsNone(node.url)

        node2 = TextNode("This is a second test node", TextType.BOLD, "http://invalid.not")
        self.assertIsNotNone(node2.url)

    def test_repr(self):
        node = TextNode("text node 1", TextType.TEXT)
        # node_string = node.__repr__
        self.assertEqual(node.__repr__(), 'TextNode(text node 1, text, None)')

if __name__ == "__main__":
    unittest.main()