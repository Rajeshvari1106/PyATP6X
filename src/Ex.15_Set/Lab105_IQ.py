# Find the first non-repeating character in a string using sets.
# swiss -> s -x , w - Answer

def non_repeat(string):
    for char in string:
        if string.count(char)==1:
            return char
    return None
result=non_repeat("nalan")
print(result)

# print("swiss".count("s"))
# print("swiss".count("w"))
# print("swiss".count("i"))

# s = set()
#
# def first_non_repeating(string):
#     for char in string:
#         if string.count(char) == 1:
#             s.add(char)
#             return char
#     return None
#
#
# print(first_non_repeating("swiss"))
# print(s)