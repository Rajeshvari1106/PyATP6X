# Find the positive number is even or add
num=int(input("Enter a number:").strip())

if num>=0:
    if num%2==0:
        print("Even")
    else:
        print("Odd")
else:
    print("negative number")


# you can write short one-liner conditions using ternary operator:
if num>=0:
    print("Even" if num%2==0 else "Odd")
else:
    print("negative number")