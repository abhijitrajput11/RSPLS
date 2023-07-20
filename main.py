# ---------------------------------Rock Paper Scissor Spock Lizard Version 2--------------------------------------
import random

l = ["rock","spock", "paper","lizard", "scissors"]

play_again = "yes"

while play_again.lower() == "yes":
    rounds = int(input("Enter the number of rounds to play: "))
    uscore = 0
    cscore = 0

    if rounds <= 0:
        print("Please enter a value greater than 0")
    else:
        for i in range(rounds):
            valid_choice = False
            while not valid_choice:
                choice = input("Enter your choice: ").lower()

                if choice in ["rock","spock", "paper","lizard", "scissors"]:
                    valid_choice = True
                else:
                    print("Please enter a valid input (rock, paper, or scissors)")

            num = l.index(choice)
            
#             print(l.index("paper"))
#             print(num)
            comp = random.randint(0, 4)

            if (num - comp) % 5 == 3 or (num - comp) % 5 == 4:
                print("You:", choice)
                print("Comp:", l[comp])
                print("---Comp WINS---")
                cscore += 1
            elif (num - comp) % 5 == 1 or (num - comp) % 5 == 2:
                print("You:", choice)
                print("Comp:", l[comp])
                print("---You WIN---")
                uscore += 1
            else:
                print("You:", choice)
                print("Comp:", l[comp])
                print("---It's a TIE---")

            print("\n")

    print("Your Score:", uscore)
    print("Computer Score:", cscore)

    if uscore > cscore:
        print("--------------You Win!---------------")
    elif uscore == cscore:
        print("It's a Tie")
    else:
        print("--------------Computer Wins-------------")
    

    play_again = input("Do you want to play again? (yes/no): ")

print("Thank you for playing!")
