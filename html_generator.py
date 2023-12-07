import json

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
    body = f"""
<body>

  <script>
    // Sample JSON data
    const treeData = {json_content};

  </script>

</body>
"""
    return body


def main():
    filename = "test_html.html"

    with open(filename, "w") as f:
        head_data = generate_head("Mindmap", "https://d3js.org/d3.v7.min.js")

        with open('mindmap.json', 'r') as file:
            json_data = json.load(file)
        json_formatted_data = json.dumps(json_data, indent=4)
        body_data = generate_body(json_formatted_data)
        data = generate_html_encapsulation(head_data+body_data)
        f.write(data)




if __name__ == "__main__":
    main()