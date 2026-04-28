inventory=["laptop",'monitor',"keyboard"]
print(f"primary item:{inventory[0]}") #laptop
inventory.append("mouse")   #adds to the end
inventory.insert(1, "webcam") #adds at index 1
inventory.pop(0)    #removes "laptop"


print(f"current stock:{inventory}")