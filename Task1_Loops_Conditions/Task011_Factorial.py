# Given a Number a number you need to calculate the factorial of that number
# n = 5
# Fact = 5×4×3*2*1 = 120
# Fact = 0 → 1, #edge case




n=5
factorial=1
if n<0:
    print("You are entering invalid negative number")
elif n==0:
    print ("Factorial of 0 is 1")
else:
    for i in range(1,n+1,1):
        factorial = factorial*i
    print("factorial of",n,"is", factorial)


