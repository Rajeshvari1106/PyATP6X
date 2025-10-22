# Grade Calculator
# Write program to calculate and display the letter grade
# for a given numerical score (e.g: A,B,C,D,E,F)
# based on following scale
# A:90-100
# B:80-90
# C:70-80
# D:60-70
# E:50-60
# Logic Building Formula
# I/p=float
# o/p=Str

score=int(input("Enter Score:").strip())
if score<0 or score >100: #0>score>100
    print("Enter valid score")
else:

    if score>=90 and score<=100:
        print("Your Grade is A")
    elif score>=80 and score<90:
        print("Your Grade is B")
    elif score>=70 and score<80:
        print("Your Grade is C")
    elif score>=60 and score<70:
        print("Your Grade is D")
    elif score<0 and score>100:
        print("Enter a valid score")
    else:
        print("your grade is F")

        # float,abc-->using "try catch"