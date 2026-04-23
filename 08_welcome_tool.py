#---STEP 1: DEFINE THE TOOL---
#'def' is short for define. 'name' is the input (parameter).
def greet_user(user_name):
    print("--------------------")
    print(f"Welcome back, {user_name}!")
    print("your developer dashboard is ready.")
    print("------------------")
    #---STEP2: CALL THE TOOL---
    #the code inside the function won't run until we "call" it.
    greet_user("Sheenaz")
    greet_user("alex")
    