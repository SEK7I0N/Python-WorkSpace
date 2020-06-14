with open("C:/Users/REX/Documents/Python_Workspace/Files/vegetables.txt","a+") as myFile:
    myFile.write("\nCabbage")
    print(myFile.read())
    myFile.seek(5)
    print(myFile.read())

