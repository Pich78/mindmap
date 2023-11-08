import json
from anytree import AnyNode
from anytree.exporter import JsonExporter

def parse_plantuml_mindmap(file_path):

  """
  Parses a PlantUML mindmap file and returns a list of nodes.

  Args:
    file_path: The path to the PlantUML mindmap file.

  Returns:
    A list of nodes.
  """
  
  previous_node_level = 0

  with open(file_path, "r") as f:
      data = f.read()
      parent_node = []
      for line in data.splitlines():
          if line != "@startmindmap" and line != "@endmindmap":
              if line.startswith("*"):
                  node_level = line.count('*')
                  node_name = line.strip('* ').strip()

                  if node_level == 1:                        
                      root = AnyNode(id=node_name)
                      parent_node.insert(0,root)
                      previous_node_level = 0
                  else:
                      this_node = AnyNode(id=node_name, parent=parent_node[previous_node_level])
                      parent_node.insert(previous_node_level,this_node)
                      previous_node_level = node_level - 1
  return root


def write_json_file(root, file_path):
  """
  Writes a list of nodes to a JSON file.

  Args:
    nodes: The list of nodes.
    file_path: The path to the JSON file.
  """

  exporter = JsonExporter(indent=4, sort_keys=False)
  #exporter.export(root)

  with open(file_path, "w") as f:
    exporter.write(root,f)
    #json.dump(nodes, f, indent=4)


if __name__ == "__main__":
  file_path = ".\mindmap.puml"
  root = parse_plantuml_mindmap(file_path)
  write_json_file(root, "mindmap.json")
