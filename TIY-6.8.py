# Date: 11 november 2025
# Name: Riyyan

# 6-8. Pets: Make several dictionaries, where each dictionary represents a differ-
# ent pet. In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.

mao = {'Type':'Cat', 'Owner_name':'Syed'}
bao = {'Type':'Dog', 'Owner_name':'Riyyan'}
cao = {'Type':'Cow', 'Owner_name':'Hassan'}
rao = {'Type':'Rat', 'Owner_name':'Syed'}

pets = [mao,bao,cao,rao]

for pet in pets:
    print(f"Pet Type: {pet['Type']}\nOwner's name: {pet['Owner_name']}\n------")