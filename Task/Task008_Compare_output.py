# **In automation, you often compare expected and actual outputs.
# Write code to check if a test case passed or failed.**
#
# expected_title = "Dashboard"
# actual_title = "Dashboard "
#
# ✅ Test Passed – Title matches
#
#
# True - why > Strip and convert them into the lowercase = both of them are equal.
#


expected_title = "Dashboard".lower().strip()
actual_title = "Dashboard ".lower().strip()

if expected_title==actual_title:
    print("Test Passed, Title Matched")
else:
    print("Test Failed")


