# --- Define your functions below! ---
class Personality():
    hiResponse =""
    whatsUpResponse = ""
    howAreYouResponse= ""


    

def intro ():
    print( "Hello i am Chatbort")
    print("Lets talk!")
    print("[INSERT FOR USE]")

#More responses
#Minigame:
# trivia game:
# R/P/S
# gues the number Minigame
#sentiment analysis (base responses on whether the user is being nice)
#Different Bort personality


    #do process input stuff


def choosePersonality():
    print("choose a personality to talk to. You can choose")
    choice = input("Mean,Nice, or Nervous ")
    return choice



# --- Put your main program below! ---
def main():
    userChoice = choosePersonality()
    print(userChoice)


    intro()
    while True:
        answer = input("(What will you say?) ")


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
