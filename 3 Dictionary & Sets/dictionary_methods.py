# # Student dictionary
student = {
    "name": "rahul kumar",
    "age": 22,
    "subjects": {
        "phy": 90,
        "chem": 85,
        "maths": 95
    }
}

# nested dictionary
print(student["subjects"]["chem"])

##dictionary methods
# 1. keys() method

print(list(student.keys()))

# 2. values() method
print(list(student.values()))

# 3. items() method
print(list(student.items()))

# 4. get() method
print(student.get("name"))

# 5. pop() method
print(student.pop("age"))

# 6. update() method
student.update({"age": 23})
print(student)