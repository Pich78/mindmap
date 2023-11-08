from anytree import Node, RenderTree

def parse_plantuml_mindmap(input_text):
    nodes = {}
    current_nodes = []
    lines = input_text.split('\n')
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith("*"):
            node_level = stripped_line.count('*')
            node_name = stripped_line.strip('* ').strip()
            if node_level <= len(current_nodes):
                parent_node = current_nodes[node_level - 1]
                new_node = Node(node_name, parent=parent_node)
                current_nodes[node_level - 1] = new_node
            else:
                parent_node = current_nodes[-1]
                new_node = Node(node_name, parent=parent_node)
                current_nodes.append(new_node)
            nodes[node_name] = new_node
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
