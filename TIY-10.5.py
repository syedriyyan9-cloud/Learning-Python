# Date: 21 november 2025
# Name: Riyyan

# 10-5. Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all the responses.

guest_no = 0
print("Press 'q' to quit")
while True:
    reason = input("Why do you like programming: ")
    if reason.lower() == 'q':
        break
    guest_no += 1
    with open('TIY-10.5.txt','a') as file:
        file.write(f"Guest#{guest_no}: {reason}\n")
