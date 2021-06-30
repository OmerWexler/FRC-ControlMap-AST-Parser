import re
import javalang
from numpy import append

FILENAME = r'E:\Desktop\workspace\software\java operation parser\ControlMap.java'

def get_file_ast(filename):
    with open(filename, 'r') as finput:
        tree = javalang.parse.parse(finput.read())

    return tree


def find_class(name, tree):
    for path, node in tree.filter(javalang.tree.ClassDeclaration):
        if node.name == name:
            return path, node


def match_expr(match_dict, invocation):
    pass


def as_pascal_case(string: str):
    pascal = ""

    for (i, char) in enumerate(string):
        if i == 0:
            char = char.upper()
        elif char.isupper():
            pascal += " "

        pascal += char

    return pascal


def parse_class_methods(class_node, button_match_dict):
    out = {}

    for method in class_node.methods:
        if method.return_type.name != 'boolean':
            continue

        relevant_buttons = []

        for _, ret in method.filter(javalang.tree.ReturnStatement):
            for _, invocation in ret.filter(javalang.tree.MethodInvocation):
                
                as_str = f"{invocation.member}("
                for _, ref in invocation.filter(javalang.tree.MemberReference):
                    as_str += f"{ref.qualifier}.{ref.member}, "

                as_str = as_str[:-2] + ")"

                button = match_expr(button_match_dict, as_str)
                
                if button != None:
                    relevant_buttons.append(button)

        out[as_pascal_case(method.name)] = relevant_buttons


def main():
    tree = get_file_ast(FILENAME)
    _, operator = find_class("Operator", tree)
    _, driver = find_class("Driver", tree)

    m = parse_class_methods(driver)
    

if __name__ == "__main__":
    main()