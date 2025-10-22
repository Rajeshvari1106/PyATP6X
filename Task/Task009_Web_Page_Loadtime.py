# **You want to check whether a web page loads within 3 seconds (performance test condition).
# **
# load_time = 4.2
# ⚠️ Page load too slow: 4.2 seconds

Load_Time=float(input("Enter webpage load time:"))
if Load_Time<=0:
    print("enter valid load time")
else:
    if Load_Time<=3:
        print("Performance good")
    elif Load_Time>3:
        print("Page load too slow")