# Date: 11 november 2025
# Name: Riyyan

# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.

favorite_places = {'syed':['pakistan','china','turkey'],
                   'riyyan':['russia','america'],
                   'hassan':['armenia','kosovo','romania'],}

for person, places in favorite_places.items():
    print(f"{person}'s favorite place:".title())
    for place in places:
        print(f"  {place}".title())
