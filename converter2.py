import anytree
import json4tree
import requests

def parse_plantuml_mindmap(filename):
    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            if line != "@startmindmap" and line != "@endmindmap":
                
            


    return anytree.AnyNode(data)

def export_tree_to_json(tree):
    return tree.to_json(indent=4)

def convert_json_to_d3_json(json_data):
    return json4tree.tree_to_d3(json_data)

def create_html_file(d3_json_data):
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Mindmap</title>
    <script src="https://d3js.org/d3.v5.min.js"></script>
</head>
<body>
    <script>
        var data = {data};

        var svg = d3.select("body").append("svg")
            .attr("width", 600)
            .attr("height", 400);

        var tree = d3.tree().data(data);

        var nodes = tree.nodes();

        var link = d3.link()
            .x((d) => d.x)
            .y((d) => d.y);

        var node = d3.node()
            .size((d) => d.size)
            .text((d) => d.data.name);

        svg.append("g")
            .attr("class", "nodes")
            .selectAll(".node")
            .data(nodes)
            .enter().append("circle")
            .attr("class", "node")
            .attr("cx", (d) => d.x)
            .attr("cy", (d) => d.y)
            .attr("r", (d) => d.size / 2);

        svg.append("g")
            .attr("class", "links")
            .selectAll(".link")
            .data(links)
            .enter().append("line")
            .attr("class", "link")
            .attr("x1", (d) => d.source.x)
            .attr("y1", (d) => d.source.y)
            .attr("x2", (d) => d.target.x)
            .attr("y2", (d) => d.target.y);

        svg.append("g")
            .attr("class", "labels")
            .selectAll(".label")
            .data(nodes)
            .enter().append("text")
            .attr("class", "label")
            .attr("x", (d) => d.x)
            .attr("y", (d) => d.y)
            .text((d) => d.data.name);
    </script>
</body>
</html>
""".format(data=d3_json_data)
    with open("mindmap.html", "w") as f:
        f.write(html)

def main():
    filename = "mindmap.puml"
    tree = parse_plantuml_mindmap(filename)
    json_data = export_tree_to_json(tree)
    d3_json_data = convert_json_to_d3_json(json_data)
    create_html_file(d3_json_data)

if __name__ == "__main__":
    main()
