from anytree import AnyNode, RenderTree
from anytree.exporter import JsonExporter

def puml_to_json(puml_file_content):

    parent_node = []    #It is the array of the last parent node; the array index is the last level
    for line in puml_file_content.splitlines():
        if line != "@startmindmap" and line != "@endmindmap":
            if line.startswith("*"):
                node_level = line.count('*')
                node_name = line.strip('* ').strip()

                if node_level == 1:                        
                    root = AnyNode(name=node_name)
                    parent_node.insert(0,root)
                else:
                    this_node = AnyNode(name=node_name, parent=parent_node[node_level-2])
                    parent_node.insert(node_level-1,this_node)  # This is the last node seen at this level

    exporter = JsonExporter(indent=2)
    #print(RenderTree(root))
    return exporter.export(root)
    



def main():
    filename = "mindmap.puml"

    with open(filename, "r") as f:
        data = f.read()
        json = puml_to_json(data)
        print(json)



if __name__ == "__main__":
    main()