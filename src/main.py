import os
import shutil
from textnode import TextNode, TextType
from generatepage import generate_page

def recursive_copy(to_path: str, from_path: str):
    copy_to_path = to_path
    copy_from_path = from_path
    for i in os.listdir(from_path):
        if os.path.isfile(os.path.join(from_path, i)):
            shutil.copy(os.path.join(from_path, i), to_path)
            continue
        new_copy_from_path = os.path.join(from_path, i)
        new_copy_to_path = os.path.join(to_path, i)
        os.mkdir(new_copy_to_path)
        recursive_copy(new_copy_to_path, new_copy_from_path)

def main():
    shutil.rmtree("./public", ignore_errors=True)
    os.mkdir("./public")
    recursive_copy("./public", "./static")
    generate_page("./content/index.md", "./template.html", "./public/index.html")

main()
