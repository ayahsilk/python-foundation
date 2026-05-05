with open("attendance.txt", "w") as file:
    file.write("sheenaz:present\n")
    file.write("ayah:present\n")
    file.write("maryam:absent\n")
    file.write("sara:absent\n")
    file.write("omar:present\n")
with open("attendance.txt","a") as file:
    file.write("danya:present\n")
    print("---FETCHING DATA FROM DISK---")
    with open("attendance.txt","r") as file:
        #we can loop through a file just like a list!
        for line in file:
            #.strip()removes the hidden '\n' at the end of lines
            print(line.strip())
