import unittest

from htmlnode import HTMLNode

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
    
    if __name__ == "__main__":
        unittest.main()