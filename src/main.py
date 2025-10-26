from textnode import TextNode, TextType

def main():
    node = TextNode("hello there", TextType.TEXT, "http://invalid.not")
    print(node)

if __name__ == "__main__":
    main()