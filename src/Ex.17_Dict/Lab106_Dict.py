my_dict={
    "name":"raji",
    "age":33,
    "role":"Tester",
    "exp":8
}

print(my_dict)
print(my_dict["role"])

# Modify element
my_dict["role"]="QA"
print(my_dict)

# Delete element
del my_dict["role"]
print(my_dict)

for key,value in my_dict.items():
    print(key,value)
    print(value)
    print(key)

print("age" in my_dict)
print("role" in my_dict)