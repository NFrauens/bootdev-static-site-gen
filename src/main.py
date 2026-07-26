from textnode import TextNode, TextType
print("hello world")

def main():
    dum = TextNode("Anchor text", TextType.LINK, "https://www.boot.dev")
    print(dum)

main()