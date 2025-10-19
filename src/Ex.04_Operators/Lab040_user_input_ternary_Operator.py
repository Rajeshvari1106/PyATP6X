from selectors import SelectSelector

user_age=(int(input("enter your Age:")))
# if user_age>+18:
#     print("Yes, you can go to goa and vote")
# else:
#     print("No, you can't go to goa and vote")

print("yes, you can vote" if user_age>=18 else"no you can't vote")
