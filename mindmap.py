import json
import plantuml
import argparse

def parse_mindmap(filename):

  with open(filename, "r") as f:
    data = plantuml.uml.MindMap(f.read())

  nodes = []
  for node in data.nodes:
    node_data = {
      "id": node.id,
      "text": node.text,
      "children": [],
    }
    for child in node.children:
      node_data["children"].append(child.id)
    nodes.append(node_data)

  return {
    "nodes": nodes,
  }

def generate_html(data):

  html = """
  <html>
    <head>
      <title>Mindmap</title>
      <script src="https://d3js.org/d3.v6.min.js"></script>
    </head>
    <body>
      <script>
        var data = {
          nodes: %s
        };

        var svg = d3.select("body").append("svg");
        svg.attr("width", 500);
        svg.attr("height", 500);

        var nodes = svg.selectAll(".node")
          .data(data.nodes)
          .enter().append("g")
          .attr("class", "node");

        var text = nodes.append("text")
          .text(function(d) { return d.text; });

        var links = nodes.append("path")
          .attr("d", function(d) {
            var start = d.x,
              end = d.children.map(function(c) { return data.nodes[c].x; });
            return "M" + start + " L" + end.join(" L");
          });

        // Collasso i nodi
        nodes.on("click", function(d) {
          d.children.forEach(function(c) {
            d3.select(".node[data-id='" + c + "']").classed("collapsed", !d.children.length);
          });
        });
      </script>
    </body>
  </html>
  """ % json.dumps(data)

  return html

def main():

    # parsing command line
    parser = argparse.ArgumentParser(description='PlantUML to dynamic Mind Map converter')
    
    parser.add_argument('-i', '--input', dest='infile', required=True, help='The input file to the script.')
    #parse and assign to the variable
    args = parser.parse_args()
    infile=args.infile

    print(infile)
    
    #data = parse_mindmap(filename)
    #html = generate_html(data)

    #with open("mindmap.html", "w") as f:
    #f.write(html)

if __name__ == "__main__":
  main()
