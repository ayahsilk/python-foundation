#---step 1: define the rooms(functions)---
def start_room():
    print("\n---THE CASTLE GATE")
    print("you stand before a massive stone gate. it is locked.")
    choice=input("do you [1]search the bushes or [2]knock on the door?")
    if choice=="1":
        print(" you found a rusty key!")
        return"treasure_room" #moving to the next room
    else:
        print("a guard wakes up and chases you away. game over loser.")
        return"End"
def treasure_room():
        print("\n---THE GOLDEN VAULT---")
        print("the rusty key fits! you are surrounded by gold.")
        choice=input("do you [1] take the gold or [2]leave it and explore further?")
        if choice=="1":
             print("the vault was a trap! the doors lock forever. game over.")
             return"end"
        else:
             print("you found a secret exit to freedom. YOU WIN YAY!")
             return "end"
#---STEP 2: THE GAME ENGINE (LOOP)---
current_room="start"
print("welcome to the python adventure engine!")
while current_room!="end":
    if current_room== "start":
        current_room= start_room()
    elif current_room=="treasure_room":
     current_room=treasure_room()
print("\n---THANKS FOR PLAYINGGG---")
     