import re
import javalang

FILENAME = r'E:\Desktop\workspace\software\java operation parser\ControlMap.java'

def get_file_ast(filename):
    with open(filename, 'r') as finput:
        tree = javalang.parse.parse(finput.read())

    return tree


def find_class(class_name, tree):
    for path, node in tree.filter(javalang.tree.ClassDeclaration):
        if node.name == class_name:
            return path, node


def get_class_methods(class_node):
    pass


def main():
    tree = get_file_ast(FILENAME)
    _, operator = find_class("Operator", tree)
    _, driver = find_class("Driver", tree)
    

if __name__ == "__main__":
    main()