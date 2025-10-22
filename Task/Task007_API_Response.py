# **Q - You receive an API response code from your test script.
# Write an if-else block to check whether the response is successful (status code 200) or not.**
#
# ```
# I/P response = 404 , O/P ❌ Failed API Request
# I/P response = 200 , O/P ✅ Passed API Request
# ```

Response_Code=int(input("Enter response code get from test script:"))
if Response_Code==200:
    print("Passed API Request")
elif Response_Code==404:
    print("Failed API Request")
else:
    print("Invalid Response Code")