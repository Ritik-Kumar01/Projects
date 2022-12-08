"""

Project Description:
This Project make use of random.randint() function of random module through which a game is made "Dice Number Guesser"
In which the user guesses the number on the dice which is generated through the random.randint(1,6) 
If the user guessed the correct answer correctly he gets 10 pts else 0 pts
User can play as many times he wants , user can exit the game by typing exit.



Group Member details:

HARSHIT KALRA Roll Number: RK22RPA12
RAUHAN KUMAR ROY Roll Number: RK22RPA32
GOURAB SEN Roll Number: RK22RPB70
"""
import random #imports random module 

def print_dice(num_on_dice,guess):
    """
    Prints the face of dice:
    1. Which the user has to guess(num_on_dice)
    2. Which is entered by the user(guess)

    Args:
        num_on_dice:
            :type num_on_dice :tuple
            :it is the value of key :dice[ai]
        guess:
            :type guess :tuple
            :it is the value of key :dice[userinput]
    """
    print("Number On Dice:")
    for i in range(len(num_on_dice)):
        print(num_on_dice[i])
    print("Number You Guessed:")
    for j in range(len(guess)):
        print(guess[j])

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
    score,n_turns=0,0
    CHOICES=["1","2","3","4","5","6","exit"]
    if choice == "exit":            #ends the game if choice entered is exit 
        pass

    else:
        while True:

            ai=random.randint(1,6)
            #random.randint(a,b) generates a number between a and b including a and b
            #in this case the number is generated between 1 and 6
            #including 1 and 6
            print()
            userinput=input("Guess the number: ") #takes the guess from the user
            if userinput=="":
                print("no input given, please give some input!!")
            elif userinput.isalpha():
                #check whether the given input is valid or not
                if userinput.lower()=="exit":           #exits the game and ends the program
                    break
                else:
                    print("Please give valid input \nThe input is either not integer or it is not between 1 to 6")
            
            elif userinput not in CHOICES:
                #check whether the given input is between 1 to 6 or not
                print("Please give valid input \nThe input is either not integer or it is not between 1 to 6")
            
            elif ai == int(userinput):      #check the number on dice is equal to number guessed or not
                print_dice(dice[ai],dice[int(userinput)])
                #prints the dices
                print("--------------RESULT---------------")
                print("Good job u guessed it right")
                print("+10 pts")
                score+=10#increases the score
                n_turns+=1 #increases the num_of_turns by one 
                print("number of turns",n_turns)
                print("score:",score)

            else:
                print_dice(dice[ai],dice[int(userinput)])  #prints the dices
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
