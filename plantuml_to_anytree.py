from anytree import AnyNode, RenderTree

def main():
    filename = "mindmap.puml"

    previous_node_level = 0

    with open(filename, "r") as f:
        data = f.read()
        parent_node = []
        for line in data.splitlines():
            if line != "@startmindmap" and line != "@endmindmap":
                if line.startswith("*"):
                    node_level = line.count('*')
                    node_name = line.strip('* ').strip()

                    print("Before")
                    print(node_level)
                    print(previous_node_level)
                    print("------")

                    if node_level == 1:                        
                        root = AnyNode(id=node_name)
                        parent_node.insert(0,root)
                        previous_node_level = 0
                    else:
                        this_node = AnyNode(id=node_name, parent=parent_node[previous_node_level])
                        parent_node.insert(previous_node_level,this_node)
                        previous_node_level = node_level - 1

                    print("After")
                    print(node_level)
                    print(previous_node_level)
                    print("------")

    
    #s0 = AnyNode(id="sub0", parent=root)
    #s0b = AnyNode(id="sub0B", parent=s0, foo=4, bar=109)
    #s0a = AnyNode(id="sub0A", parent=s0)
    #s1 = AnyNode(id="sub1", parent=root)
    #s1a = AnyNode(id="sub1A", parent=s1)
    #s1b = AnyNode(id="sub1B", parent=s1, bar=8)
    #s1c = AnyNode(id="sub1C", parent=s1)
    #s1ca = AnyNode(id="sub1Ca", parent=s1c)    
    #tree = parse_plantuml_mindmap(filename)
    print(RenderTree(root))


if __name__ == "__main__":
    main()