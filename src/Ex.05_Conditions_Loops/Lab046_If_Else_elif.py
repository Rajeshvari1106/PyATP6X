# Problem find the max between 3 numbers

# Logic Building
# I/p=int(n1,n2,n3)
# o/p=int or string with the max number

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))
if num1>=num2 and num1>=num3:
    print("maximum",num1)
elif num2>=num1 and num2>=num3:
    print("maximum",num2)
else:
    print("maximum",num3)

