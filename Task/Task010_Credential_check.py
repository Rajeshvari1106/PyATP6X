# Q4**  - Check if the user can log in based on correct username and password.**
#
# I/p
#
# ```
# username = "admin"
# password = "1234"
# ```
# O/p
# ✅ Login Successful
#
#
# For the Fail condition Other O/P = ❌ Invalid Credentials
#

import getpass
username=input("Enter your Username:".strip())
Password=input("Enter your Password:".strip())
if username=="admin" and Password=="1234":
    print("Login Successful")
else:
    print("Invalid Credentials")