secret_password="python_pro"
print("welcome to the secure vault.")
guess=input("enter the secret password:")
if guess==secret_password:
    print("ACCESS GRANTED!")
    print("welcome, agent. your mission is to master lesson5.")
else: 
    print("ACCESS DENIED!")
print("security has been alerted. please try again.")
