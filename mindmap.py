import json
import argparse
from html_generator import *
import os

def main():

    # parsing command line
    parser = argparse.ArgumentParser(description='PlantUML to dynamic Mind Map converter')
    
    parser.add_argument('-i', '--input', dest='infile', required=True, help='The input PUML file to be converted by the script.')
    parser.add_argument('-o', '--output', dest='outfile', required=False, help='The output HTML with the mindmap.')
    #parse and assign to the variable
    args = parser.parse_args()

    if not args.outfile:        
      root, ext = os.path.splitext(args.infile)      
    else:
      root, ext = os.path.splitext(args.outfile)

    output_file_name = root + ".html"

    with open(output_file_name, "w") as output_file:
        head_data = generate_head("Mindmap", "https://d3js.org/d3.v7.min.js")

        source_file_name = args.infile
        with open(source_file_name, "r") as source_file:
          data = source_file.read()
          json = puml_to_json(data)

          body_data = generate_body(json)
          data = generate_html_encapsulation(head_data+body_data)
          output_file.write(data)

if __name__ == "__main__":
  main()
