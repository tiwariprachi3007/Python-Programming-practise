#create a new file"practice.txt"using python . add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java
# I like programming in Java

## waf that replaces all occurrences of "java" with "python" in above file

# Step 1: Write the initial content
with open("practice.txt", "w") as f:
    f.write("Hi everyone\n")
    f.write("we are learning File I/O\n")
    f.write("using Java\n")
    f.write("I like programming in Java\n")

# Step 2: Read the content
with open("practice.txt", "r") as f:
    data = f.read()

# Step 3: Replace 'Java' with 'Python'
new_data = data.replace("Java", "Python")
print(new_data)

# Step 4: Write the updated content back
with open("practice.txt", "w") as f:
    f.write(new_data)
