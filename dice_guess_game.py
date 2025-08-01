import random

def print_dice(n,m):
    for i in range(len(n)):
        print(n[i],"  ",m[i])

if __name__=="__main__":
    print("DICE GUESS GAME")
    print("Rules:")
    print("1) AI throws dice")
    print("2) User needs to guess the number on dice")
    print("3) if user guess it correctly +10 pts")
    print("4) if user guess it wrong 0 pts added")
    print("5) user can play this game as many times as he wants")
    print("6) To exit the game while playing press exit to quit the game in between")
    print()
    print("press any key to start and 'exit' to quit:")
    print()
    dice = {
        1: (
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        )
    }
    choice=input("Press Enter To Start or Exit To Quit: ").lower()

    if choice == "exit":
        pass

    else:
        score,n_turns=0,0
        while True:

            ai=random.randint(1,6)
            print()
            userinput=input("Guess the number: ")
            if userinput=="":
                print("no input given, please give some input!!")

            elif userinput.isalpha():
                if userinput.lower()=="exit":
                    break
                else:
                    print("wrong input or no input given, please give a valid input")
            
            elif userinput != "6" and userinput != "5" and userinput!="4" and userinput!="3" and userinput!="2" and userinput!="1" and userinput!="exit":
                print("wrong input or no input given, please give a valid input")
            
            elif ai == int(userinput):
                print_dice(dice[ai],dice[int(userinput)])
                print("--------------RESULT---------------")
                print("Good job u guessed it right")
                print("+10 pts")
                score+=10
                n_turns+=1
                print("number of turns",n_turns)
                print("score:",score)

            else:
                print_dice(dice[ai],dice[int(userinput)])
                n_turns+=1
                print("--------------RESULT---------------")
                print("oops! you guessed the wrong number")
                print("number of turns",n_turns)
                print("score:",score)
print()
print("you played",n_turns,"times")
print("your final scores is :",score)
print("Thank you for playing this game!")
print("Have a nice day")
