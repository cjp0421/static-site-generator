import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_unset_is_none(self):
        node = HTMLNode("a", "Click me!")

        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_props(self):
        props = {
            "href": "http://invalid.not",
            "target":"_blank"
        }

        childNode = HTMLNode("div")

        node = HTMLNode("a", "Click me!", childNode, props)

        self.assertDictEqual(node.props, props)

    def test_props_to_html(self):

        childNode = HTMLNode("div")

        props = {
            "href": "http://invalid.not",
            "target":"_blank"
        }

        props_string = f' href="http://invalid.not" target="_blank"'

        node = HTMLNode("a", "Click me!", childNode, props)

        self.assertEqual(node.props_to_html(), props_string)

    def test_repr(self):
        node = HTMLNode("a")

        self.assertEqual(node.__repr__(), 'Tag: a, Value: None, Children: None, Props: None')
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        props = {
            "href": "http://invalid.not",
            "target":"_blank"
        }
        node = LeafNode("a", "Click me!", props)
        self.assertEqual(node.to_html(), '<a href="http://invalid.not" target="_blank">Click me!</a>')

    def test_empty_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None).to_html()
    
    def test_leaf_to_html_div_no_tag(self):
        node = LeafNode(None, "PLAIN TEXT")
        self.assertEqual(node.to_html(), "PLAIN TEXT")

    if __name__ == "__main__":
        unittest.main()