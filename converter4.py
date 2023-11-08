import re
from anytree import Node, RenderTree

def parse_plantuml_mindmap(input_text):
    nodes = {}
    current_nodes = []
    lines = input_text.split('\n')
    for line in lines:
        match = re.match(r'\s*[*]{1,}\s+(.+)', line)
        if match:
            node_name = match.group(1)
            node_level = line.count('*')
            if node_level <= len(current_nodes):
                current_nodes[node_level - 1] = Node(node_name, parent=current_nodes[node_level - 2])
            else:
                parent_node = current_nodes[node_level - 2]
                current_nodes.append(Node(node_name, parent=parent_node))
            nodes[node_name] = current_nodes[node_level - 1]
    return nodes

plantuml_text = """
@startmindmap
* Udo
** Marc
*** Lian
** Dan
*** Jet
**** John
*** Jan
**** Bob
***** Alice
****** Eve
**** Joe
@endmindmap
"""

nodes = parse_plantuml_mindmap(plantuml_text)

for pre, fill, node in RenderTree(nodes["Udo"]):
    print(f"{pre}{node.name}")
