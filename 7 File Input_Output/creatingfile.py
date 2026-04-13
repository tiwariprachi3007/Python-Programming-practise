#create a new file"practice.txt"using python . add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java
# I like programming in Java

with open("practice.txt","w") as f:
    f.write("Hi everyone\n")
    f.write("we are learning File I/O\n")
    f.write("using Java\n")
    f.write("I like programming in Java\n")