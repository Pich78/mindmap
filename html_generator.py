def generate_html_encapsulation(data):
    starting_text =  """<!DOCTYPE html>
<html lang="en">
"""
    
    closing_tag = """
</html>"""

    return (starting_text + data + closing_tag)



def main():
    filename = "test_html.html"

    with open(filename, "w") as f:
        data = generate_html_encapsulation("")
        f.write(data)




if __name__ == "__main__":
    main()