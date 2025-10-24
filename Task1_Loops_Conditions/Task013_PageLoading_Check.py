# Simulate a page loading check using a while loop.
# If page_loaded becomes True within 5 seconds, print success; else timeout.
#
# Hint: Use a counter (like wait_time) and break condition.
#
# import time
# wait_time=0
# while wait_time<=5:
#     print(f"wait_time{wait_time:.2f}seconds, Page Loading......")
#     if loading_time=5:
#     time.sleep(1)
#     wait_time+=1
#     break
#
# if wait_time>5:
#     print("Time out")

import time
import random

page_loaded = False
wait_time = 0

while wait_time < 5:
    # Simulate checking if the page is loaded
    page_loaded = random.choice([False, False, False, True])  # Randomly succeeds

    if page_loaded:
        print("✅ Page loaded successfully!")
        break

    time.sleep(1)  # Wait for 1 second before checking again
    wait_time += 1
    print(f"Waiting... {wait_time} seconds")

if not page_loaded:
    print("⏰ Timeout: Page did not load within 5 seconds.")