# Q - Create a function which will take a positive number from the user and perform square of the number?
#
# i/o = 3
#
# o/p = 9
def square_of_number(num):
    if num > 0:
        return num ** 2
    else:
        print("Invalid Number")


result=square_of_number(int(input("Enter a number")))
print(result)

