# Date: 28 october 2025 name riyyan

# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger
# dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.


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

