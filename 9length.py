//find length of string
def length(string):
    if string == "":
       return 0
    return 1 + length(string[1:])
    
string = "Hello World"
# here space is also consider       

print("The string is ",string)
print("Length of ",string," is",length(string))
