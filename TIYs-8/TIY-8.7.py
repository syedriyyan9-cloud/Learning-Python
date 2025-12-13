# Date: 13 november 2025
# Name: Riyyan

# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.

def make_album(name, album, no_of_songs = None):
    music_album = {'artist_name': name, 'artist_album':album}
    if no_of_songs:
        music_album['songs'] = no_of_songs
        return music_album
    return music_album

print(make_album('Atif Aslam', 'Humain Pyar Hai Pakistan Se'))
print(make_album('Ali Zafar','Aik Qaum, Aik Manzil'))
print(make_album('Bilal Saeed','Snapchat Story'))
print(make_album('Imran Khan','Bewafa', 15))