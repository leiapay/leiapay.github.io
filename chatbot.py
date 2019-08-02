# --- Define your functions below! ---
class Personality():
    hiResponse =""
    whatsUpResponse = ""
    howAreYouResponse= ""


    def processInput (self,response):
        if response == "Hi":
            print(self.hiResponse)
        elif response == "Whats up?":
            print(self.whatsUpResponse)
        elif response == "How are you?":
            print(self.howAreYouResponse)
        else :
             print(self.otherResponse)

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

    niceRobot = Personality ()
    niceRobot.hiResponse = ("Hello i am Chatbort, It's so nice to meet you!")
    niceRobot.whatsUpResponse = ("Oh, I'm just talking to the most intresting person")
    niceRobot.howAreYouresponse = ("oh, how lovely")
    niceRobot.otherResponse = ("Sorry love, i cant help you with that")

    meanRobot = Personality()
    meanRobot.hiResponse= (" Can you leave?")
    meanRobot.whatsUpResponse= ("Dont speak to me")
    meanRobot.howAreYouResponse = ("Does it seem like i care")
    meanRobot.otherResponse = ("I dont care")

    nervousRobot = Personality()
    nervousRobot.hiResponse= (" Um, hi ...")
    nervousRobot.whatsUpResponse= ("Um, its been a long week...")
    nervousRobot.howAreYouResponse = ("I dont think you wanna know")
    nervousRobot.otherResponse = ("um, im sorry can you repeat that")
    intro()
    while True:
        answer = input("(What will you say?) ")
        if (userChoice == "Nice"):
            niceRobot.processInput(answer)
        elif (userChoice == 'Mean'):
            meanRobot.processInput(answer)
        elif (userChoice == "Nervous"):
            nervousRobot.processInput(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
