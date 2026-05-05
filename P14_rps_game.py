import random
def play_game():
    options=["rock","paper","scissors"]
    user_score=0
    computer_score=0
    print("---welcome to the python battle arena---")
    while True:
    user_choice=input("\nchoose rock, paper, or scissors(or type 'quit' to exit):").lower()
    if user_choice=='quit':
        break
    if user_choice not in options:
        print("invalid choice! please try again.")
    continue
#computer makes a random choice
computer_choice=random.choice(options)
 print(f"computer chose:{computer_choice}")
#determine the winner
if user_choice==computer_choice:
   print("it's a tie!")
elif (user_choice=="rock" and computer_choice=="scissors") or \
     (user_choice=="paper" and computer_choice=="rock") or \
     (user_choice=="scissors" and computer_choice=="paper"):
    print("you win!")
    user_score+=1
else:
    print("computer wins!")
    computer_score+=1
print(f"score: you {user_score} - computer {computer_score}")
print("\n---final score---")
print(f"you: {user_score}")
print(f"computer: {computer_score}")
if user_score>computer_score:
    print("congratulations! you are the champion!")
elif computer_score>user_score:
    print("computer wins the game! better luck next time.")
else:   print("the game ends in a tie! well played.")       
play_game()