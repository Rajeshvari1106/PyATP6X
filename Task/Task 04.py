# write a python pgm to calculate the area of circle
# Given its radius using formula
# '''area=3.14*r^2'''

# Radius=float(input("enter your Radius:"))
# # I/p-->float
# # O/p-->string formatted output of area
# area=str(3.14*Radius*Radius)
# print(area)
# print(type(area))

# Logic building formula
#step 1:
# figure out input and output
# input-->r-->datatype-->float
# pi=3.14
# power-->pow() or **-->any
# o/p-->string-->float-area, print area

#step2
#rough logic=area=3.14*pow(r,2)

# step3
radius=float(input("enter your radius:"))
print(radius)
# area=3.14*(radius**2)
radius=3.14*(pow(radius,2))

# print('Are of the circle is-->',area)

# String Data formatting
print("Area of the circle is->{area:2f}")