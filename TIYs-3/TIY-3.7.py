# date 28 october 2025 name riyyan

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.


guests = ["riyan", "hassan", "syed"]

guests[2] = "kamran"

guests.insert(0,"kashif")
guests.insert(int(len(guests)/2), "ilyas")
guests.append("noman")

print(f"I have found a bigger table so {guests[0]} is invited over for dinner")
print(f"I have found a bigger table so {guests[1]} is invited over for dinner")
print(f"I have found a bigger table so {guests[2]} is invited over for dinner")
print(f"I have found a bigger table so {guests[3]} is invited over for dinner")
print(f"I have found a bigger table so {guests[4]} is invited over for dinner")
print(f"I have found a bigger table so {guests[5]} is invited over for dinner")

print("I can only invite 2 people over for dinner as bigger table would not arrive on time.")

not_invited = guests.pop()
print(f"Writing this to let you know that i have to cancel the dinner with you {not_invited}. maybe next time?")
not_invited = guests.pop()
print(f"Writing this to let you know that i have to cancel the dinner with you {not_invited}. maybe next time?")
not_invited = guests.pop()
print(f"Writing this to let you know that i have to cancel the dinner with you {not_invited}. maybe next time?")
not_invited = guests.pop()
print(f"Writing this to let you know that i have to cancel the dinner with you {not_invited}. maybe next time?")

print(f"{guests[0]} you are still invited for dinner")
print(f"{guests[1]} you are still invited for dinner")

del guests[0]
del guests[0]

print(guests)
