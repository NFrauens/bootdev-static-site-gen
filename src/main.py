import os
import shutil
import sys
from textnode import TextNode, TextType
from generatepage import generate_pages_recursive

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
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    shutil.rmtree("./docs", ignore_errors=True)
    os.mkdir("./docs")
    recursive_copy("./docs", "./static")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

main()
