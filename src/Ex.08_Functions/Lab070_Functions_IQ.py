# Create a pgm to sum of 3 number from the user input
# If user doesn't enter any number, use default as 100,200,300
a=int(input("Enter a number:"))
b=int(input("Enter b number:"))
c=int(input("Enter c number:"))
def sum_of_3_numbers(a1=100,b1=200,c1=300):
    return a1+b1+c1
result=sum_of_3_numbers(3,4,5)
result0=sum_of_3_numbers(a,b,c)
result1=sum_of_3_numbers()
result2=sum_of_3_numbers(a1=10)
result3=sum_of_3_numbers(a1=10,b1=b)

print(result)
print(result0)
print(result1)
print(result2)
print(result3)
