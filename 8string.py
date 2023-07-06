fname = input("Enter file name: ")
with open(fname, 'r') as f:
    content = f.read()
    capitalized_content = content.capitalize()
    print(capitalized_content)
