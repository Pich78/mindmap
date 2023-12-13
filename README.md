# mindmap
A python script that creates a HTML file with a mind map starting from [Plant UML](https://plantuml.com) format.

To add the ability to collapse and expand branches, I use the D3.js library

## Usage

`python mindmap.py -i <input file in plant uml mind map format> [ -o output html file name ]`

If the output file name is missing, the generated .html file will be `input_file_name.html`

## Inspiration:

[Stack Overflow](https://stackoverflow.com/questions/60107431/d3-tree-with-collapsing-boxes-using-d3-version-4)

## d3js resources:

Example to learn to work with D3 nodes: [D3 Noob](http://www.d3noob.org/2014/01/tree-diagrams-in-d3js_11.html)

#### Interesting articles related to d3.js

[Margin Convention](https://observablehq.com/@d3/margin-convention)

[More on margins](https://gist.github.com/jsoma/71bee11bbe6b73887bca4138fd4d2442)

[Enter, update, exit introduction](https://medium.com/@c_behrens/enter-update-exit-6cafc6014c36)

## Libraries

[Anytree](https://pypi.org/project/anytree/)

I use this library to store the PUML file into a tree structure.
I also use the `jsonexporter` to export the tree into a JSON file.

To install:

`python -m pip install anytree`

