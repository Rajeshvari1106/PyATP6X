# Write a pgm for if age is 21 can to club otherwise no
from idlelib.debugger_r import close_subprocess_debugger

# Step1:
# i/p=age(int)
# o/p=string

# step2(Rough logic)
# age>= go to club
# age<21=cant go

# step3:write the logic
age=int(input("enter your age:".strip()))
if age<=0 or age>130:
    print("Enter a valid age")
else:
    if age>=21:
        print("Yes, you can go to club")
    else:
        print("No, you can't go to club")

# Step4:edge cases check
'''we should consider edge cases such as:
Negative ages or extreemly high values-->Program will break.
Non-Numeric Input-ABC
Age which is valid. >130
'''

# Step5: Optimise the code
# Handle all edge cases: