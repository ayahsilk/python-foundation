#---THE TICKET ENGINE---
def submit_ticket():
    print("\n---NEW TICKET---")
    name=input("Your name:")
    issue=input("what is the problem?")
    #'a'(append)adds the new ticket to the end of the file
    with open("support_log.txt","a")as file:
        file.write(f"NAME:{name}|ISSUE:{issue}\n")
        print("ticket submitted successfully!")
def view_tickets():
    print("\n---OPEN TICKET---")
    try:
        #'r'(read)opens the file to view the contents
        with open("support_log.txt","r") as file:
            print(file.read())
    except FileNotFoundError:
         print("no tickets found yet.")
while True:
    choice=input("\n[1] new ticket [2] view tickets [3] quit:")
    if choice=="1":
        submit_ticket()
    elif choice=="2":
        view_tickets()
    elif choice=="3":
        break