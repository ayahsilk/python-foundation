import random
from requests import options
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
    computer_choice=random.choice(  options)
    print(f"computer chose:{computer_choice}")
    #determine the winner
    # if user_choice==computer_choice:
        print("it's a tie!")
elif (user_choice=="rock" and computer_choice=="scissors") or \
     (user_choice=="paper" and computer_choice=="rock") or \
     (user_choice=="scissors" and computer_choice=="paper"):
    print("you win!")
    user_score+=1
else:
    print("computer wins!")
    computer_score+=1
print(f"scoreboard-> you: {user_score}|computer: {computer_score}")
save the final score to a file (lesson file handling)
with open("rps_scores.txt","a") as f:
    f.write(f"final score-> you: {user_score}|computer: {computer_score}\n")
print("\nthanks for playing! your results have been saved to rps_scores.txt")
play_game()
