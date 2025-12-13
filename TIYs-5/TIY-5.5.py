# Date: 2 november 2025
# Name: Riyyan

# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-
# else chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed
# for the appropriate color alien.

alien_color = 'yellow'

if alien_color == 'green':
    print("+5 points")
elif alien_color == 'yellow':
    print("+10 points")
elif alien_color == 'red':
    print("+15 points")

if alien_color == 'yellow':
    print("+5 points")
elif alien_color == 'red':
    print("+10 points")
elif alien_color == 'green':
    print("+15 points")

if alien_color == 'red':
    print("+5 points")
elif alien_color == 'green':
    print("+10 points")
elif alien_color == 'yellow':
    print("+15 points")