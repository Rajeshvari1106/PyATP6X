# a={1,2,3}
# b={3,4,5}
#
# print(a|b)
# print(a.union(b))
# print(a&b)
# print(a.intersection(b))
#
# # difference
# print(a-b)
# print(b-a)
#
# # common element removed
# print(a^b)


set1={1,2,3}
set2={4,5,6}
myset=set1.union(set2)
print(myset)
myset1=set1.intersection(set2)
print(myset1)

set3={1,2,3,4,5}
set4={4,5,6,7,8}
myset=set3.intersection(set4)
print(myset)

myset=set3.difference(set4)
print(myset)
myset=set4.difference(set3)
print(myset)