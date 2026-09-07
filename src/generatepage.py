import os
from markdowntohtmlnode import markdown_to_html_node
from splitnodedelimiter import extract_title
import pathlib

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = (open(from_path)).read()
    template_copy = (open(template_path)).read()
    HTML_string = (markdown_to_html_node(markdown)).to_html()
    title = extract_title(markdown)
    print(basepath)
    new_page = ((template_copy.replace("{{ Title }}", title)).replace("{{ Content }}", HTML_string).replace('href="/', f'href="{basepath}')).replace('src="/', f'src="{basepath}')
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, mode="w") as f:
        f.write(new_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for i in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, i)):
            generate_page(os.path.join(dir_path_content, i), template_path, pathlib.Path(dest_dir_path, "index.html"), basepath)
            continue
        generate_pages_recursive(os.path.join(dir_path_content, i), template_path, os.path.join(dest_dir_path, i), basepath)