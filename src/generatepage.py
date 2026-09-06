import os
from markdowntohtmlnode import markdown_to_html_node
from splitnodedelimiter import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = (open(from_path)).read()
    template_copy = (open(template_path)).read()
    HTML_string = (markdown_to_html_node(markdown)).to_html()
    title = extract_title(markdown)
    new_page = (template_copy.replace("{{ Title }}", title)).replace("{{ Content }}", HTML_string)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, mode="w") as f:
        f.write(new_page)