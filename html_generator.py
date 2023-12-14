import json
from plantuml_to_anytree import puml_to_json

def generate_html_encapsulation(data):
    html = """<!DOCTYPE html>
<html lang="en">
{}
</html>
    """.format(data)
    return html



def generate_head(title, script_url):
    head = f'''
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <script src="{script_url}"></script>
  <style>
    .node {{
      cursor: pointer;
    }}

    .node circle {{
      fill: #fff;
      stroke: steelblue;
      stroke-width: 3px;
    }}

    .node rect {{
      fill: #fff;
      stroke: steelblue;
      stroke-width: 3px;
    }}

    .node text {{
      font: 12px sans-serif;
    }}
    .link {{
      fill: none;
      stroke: #ccc;
      stroke-width: 2px;
    }}
  </style>
</head>
'''
    return head

def generate_body(json_content):
    body = f'''
<body>

  <script>
    // Sample JSON data
    const treeData = {json_content};
  // ************** Generate the tree diagram  *****************
  var margin = {{top: 20, right: 50, bottom: 20, left: 50}},
  width = 960 - margin.right - margin.left,
  height = 500 - margin.top - margin.bottom;
  
  var i = 0;

  // Create SVG container
  const svg = d3.select("body").append("svg")
    .attr("width", width + margin.right + margin.left)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", `translate(${{margin.left}},${{margin.top}})`);

  // Create hierarchical data structure
  const root = d3.hierarchy(treeData);
  var tree = d3.tree().size([height, width]);
  tree(root);

  // Create links
  const link = svg.selectAll(".link")
    .data(root.links())
    .enter().append("path")
    .attr("class", "link")
    .attr("d", d3.linkHorizontal()
      .x(d => d.y)
      .y(d => d.x)
    );

  // Create nodes
  const node = svg.selectAll(".node")
    .data(root.descendants())
    .enter().append("g")
    .attr("class", "node")
    .attr("transform", d => `translate(${{d.y}},${{d.x}})`);

  // Debug print of structure
  console.log("Nodes are: "); 
  console.log(node); 

  // Add text to nodes
  const text = node.append("text")
    .attr("y", 4)
    .attr("x", -10)
    .attr("text-anchor", d => ("start"))
    .text(d => d.data.name);

  // Add rectangles to nodes
  // The box position shift shall be half of the size
  node.insert("rect", "text")
    .attr("x", -20)
    .attr("y", -10)
    .attr("width", d => text.filter(t => t === d).node().getComputedTextLength() + 20)
    .attr("height", 20);

  </script>

</body>
'''
    return body



def main():
    output_file_name = "test_html.html"

    with open(output_file_name, "w") as output_file:
        head_data = generate_head("Mindmap", "https://d3js.org/d3.v7.min.js")

        source_file_name = "mindmap.puml"
        with open(source_file_name, "r") as source_file:
          data = source_file.read()
          json = puml_to_json(data)

        #with open('mindmap.json', 'r') as file:
        #    json_data = json.load(file)
        #json_formatted_data = json.dumps(json_data, indent=4)
          body_data = generate_body(json)
          data = generate_html_encapsulation(head_data+body_data)
          output_file.write(data)




if __name__ == "__main__":
    main()