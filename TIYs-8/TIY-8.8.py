# Date: 13 november 2025
# Name: Riyyan

# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

def make_album(name, album):
    music_album = {'artist_name': name, 'artist_album':album}
    return music_album

while True:
    print("Enter 'q' to exit")
    artist = input("Enter an artist's name: ")
    if artist.lower() == 'q':
        break
    title = input("Enter album title: ")
    if title.lower() == 'q':
        break
    print(make_album(artist,title))