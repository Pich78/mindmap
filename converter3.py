import anytree
import re

def parse_mindmap(filename):
    with open(filename) as f:
        content = f.read()

    root = anytree.Node("Root")
    level = 0
    for match in re.finditer(r"^(\*|\*\*) (.+)$", content):
        level = match.lastindex[1]
        name = match.group(2)

        if level == 0:
            child = anytree.Node(name)
            root.children.append(child)
        elif level > 0:
            children = []
            for child_name in name.split(" "):
                children.append(parse_mindmap(child_name, level - 1))
            root.children[-1].children.extend(children)

    return root


if __name__ == "__main__":
    root = parse_mindmap("mindmap.puml")
    print(anytree.RenderTree(root))
