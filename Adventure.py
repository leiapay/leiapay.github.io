
# Update this text to match your story.
from random import *
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)
aRandomNumber = randint(1, 10)

print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
user_input = input()
if user_input == "left":

    print(" You've stepped on a wire, and new path appeared showing that you could go straight or right")
    print (" After walking for a while the light is suddenly turned off")
    user_left = input()
    if user_left == "straight":
        print("five seconds pass and you feel the floor shaking, and you start to freak out")
        print("...")
        print("the floor begins to split open and you are being sucked to the center of the earth.")
        print("YOU LOSE")

    elif user_left == "right":
        print(" as you wonder in the dark you come across another wire which triggers the lights to be turned on.")
        print("to Your suprise you come across to a door, and reach for the handle and uncover...")
        print (" a room full of clowns")
        print(" the clowns start walking closer to you as the seconds")
        print("A clown grabs you from behind, when you weren't watching")
        print("They start chocking you")
        print(" ")
        print("Your vision become blurry,another clown starts to approach you")
        print(" and asks you pick a number from 1 to 10")
        print("If you pick the right number you get to live or then bye bye")
        guess= input("One to ten ")

        if not guess.isnumeric(): # checks if a string is only digits 0 to 9
            print("BYE BYE YOU ARE DEAD!")
        else:
            guess= int(guess)
            if guess== aRandomNumber:
                print("You get to live another day")
                print("*you walked away slowly and you stayed in the maze for your rest of your life. THE END")
            else:
                print("BYE BYE")




    # Continue code to finish story.

elif user_input == "right":
    print("You choose to go right and ...") # Update to match your story.
    print(" You've stepped on a wire, and new path appeared showing that you could go straight or left")
    print (" After walking for a while the light is suddenly turned off")
    user_right = input()
    if user_right == "straight":
        print("five seconds pass and you feel the floor shaking, and you start to freak out")
        print("...")
        print("the floor begins to split open and you are being sucked to the center of the earth.")
        print("YOU LOSE")

    elif user_right == "left":
        print(" as you wonder in the dark you come across another wire which triggers the lights to be turned on.")
        print("to Your suprise you come across to a door, and reach for the handle and uncover...")
        print (" a room full of clowns")
        print(" the clowns start walking closer to you as the seconds")
        print("A clown grabs you from behind, when you weren't watching")
        print("They start chocking you")
        print(" ")
        print("Your vision become blurry,another clown starts to approach you")
        print(" and asks you pick a number from 1 to 10")
        print("If you pick the right number you get to live or then bye bye")
        guess= input("One to ten ")

        if not guess.isnumeric(): # checks if a string is only digits 0 to 9
            print("BYE BYE YOU ARE DEAD!")
        else:
            guess= int(guess)
            if guess== aRandomNumber:
                print("You get to live another day")
                print("*you walked away slowly and you stayed in the maze for your rest of your life. THE END")
            else:
                print("BYE BYE")


    # Continue code to finish story.
