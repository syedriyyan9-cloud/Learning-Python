# Date: 28 october 2025 name riyyan

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end
# of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# in your list.

guests = ["riyan", "hassan", "syed"]
print(f"{guests[0]} is coming for dinner")
print(f"{guests[1]} is coming for dinner")
print(f"{guests[2]} cannot make it to dinner")
guests[2] = "kamran"
print(f"and in its place {guests[2]} is coming over for dinner")

print(f"{guests[0]} is invited over for dinner")
print(f"{guests[1]} is invited over for dinner")
print(f"{guests[2]} is invited over for dinner")


