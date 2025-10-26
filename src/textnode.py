from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__(self, text, text_type, url = None):
        if not isinstance(text_type, TextType):
            raise TypeError("text_type must be a TextType")
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, textNode2):
        if not isinstance(textNode2, TextNode):
            return False
        return (
            self.text == textNode2.text and
            self.text_type == textNode2.text_type and
            self.url == textNode2.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    