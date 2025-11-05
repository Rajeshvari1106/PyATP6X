# Q - Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
# i/p - int side1 == side2 =side3 → isoceles
# o/p = result in string - iso, eq, scalene

side1=int(input("Enter value of Side1:"))
side2=int(input("Enter value of Side2:"))
side3=int(input("Enter value of Side3:"))
def len_of_triangle(side1,side2,side3):
    if side1<=0 or side2<=0 or side3<=0:
        print("Please enter valid numbers")
    elif side1==side2==side3:
        print("This is Equilater Triangle")
    elif side1==side2 or side1==side3 or side2==side3:
        print("This is Isoceles Triangle")
    else:
        print("This is Scalane Triangle")

len_of_triangle(side1,side2,side3)