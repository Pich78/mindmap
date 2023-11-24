# mindmap
A python script that creates a HTML file with a mind map starting from [Plant UML](https://plantuml.com) format.

To add the ability to collapse and expand branches, I use the D3.js library

Inspiration from here: [Stack Overflow]([https://stackoverflow.com/questions/67480339/programmatically-opening-d3-js-v4-collapsible-tree-nodes](https://stackoverflow.com/questions/60107431/d3-tree-with-collapsing-boxes-using-d3-version-4)https://stackoverflow.com/questions/60107431/d3-tree-with-collapsing-boxes-using-d3-version-4)

Example to learn to work with D3 nodes: [D3 Noob](http://www.d3noob.org/2014/01/tree-diagrams-in-d3js_11.html)

#### Interesting articles related to d3.js
[Margin Convention](https://observablehq.com/@d3/margin-convention)
[More on margins](https://gist.github.com/jsoma/71bee11bbe6b73887bca4138fd4d2442)


#### Libraries

[Anytree](https://pypi.org/project/anytree/)

I use this library to store the PUML file into a tree structure.
I also use the `jsonexporter` to export the tree into a JSON file.

To install:

`python -m pip install anytree`

[json4tree](https://pypi.org/project/json4tree/)

I use this library to transform a JSON into a D3 hierarchy JSON.

To install:

`python -m pip install json4tree`
