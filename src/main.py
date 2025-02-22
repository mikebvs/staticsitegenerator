import textnode
import parsemarkdown

def main():
    text_node = textnode.TextNode("Hello, world!", textnode.TextType.NORMAL, "http://example.com")


    #text_image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    #text_image = "This is text with a ![rick roll]() and ![obi wan]()"
    #print(parsemarkdown.extract_markdown_images(text_image))
    #text_link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    #text_link = "This is text with a link [to boot dev]() and [to youtube]()"
    #print(parsemarkdown.extract_markdown_url(text_link))

    #node = textnode.TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", textnode.TextType.NORMAL)
#
    #print(parsemarkdown.split_nodes_image(node))
#
    #node = textnode.TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", textnode.TextType.NORMAL)
#
    #print(parsemarkdown.split_nodes_url(node))

    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

    print(parsemarkdown.text_to_textnodes(text))

if __name__ == "__main__": 
    main()