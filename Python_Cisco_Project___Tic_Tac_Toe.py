
loop=True
count=0
a1=" "
a2=" "
a3=" "
b1=" "
b2=" "
b3=" "
c1=" "
c2=" "
c3=" "

row0 = "    1 | 2 | 3 |"

def showBoard():
    global row0,a1,a2,a3,b1,b2,b3,c1,c2,c3
    row1 = " A "+" "+a1+" "+"|"+" "+a2+" "+"|"+" "+a3+" "+"|"
    row2 = " B "+" "+b1+" "+"|"+" "+b2+" "+"|"+" "+b3+" "+"|"
    row3 = " C "+" "+c1+" "+"|"+" "+c2+" "+"|"+" "+c3+" "+"|"

    print(row0)
    print(row1)
    print(row2)
    print(row3)
    print("\n")

def crossChoiceFunc():
    global a1,a2,a3,b1,b2,b3,c1,c2,c3
    crossChoice = input("Team Crosses: Enter the Row Letter and Column Number (E.G A2)\n")

    if crossChoice == "A1" and a1 == " ":
        a1 = "x"
    if crossChoice == "A2" and a2 == " ":
        a2 = "x"
    if crossChoice == "A3" and a3 == " ":
        a3 = "x"
    if crossChoice == "B1" and b1 == " ":
        b1 = "x"
    if crossChoice == "B2" and b2 == " ":
        b2 = "x"
    if crossChoice == "B3" and b3 == " ":
        b3 = "x"
    if crossChoice == "C1" and c1 == " ":
        c1 = "x"
    if crossChoice == "C2" and c2 == " ":
        c2 = "x"
    if crossChoice == "C3" and c3 == " ":
        c3 = "x"
    showBoard()

def noughtChoiceFunc():
    global a1,a2,a3,b1,b2,b3,c1,c2,c3
    noughtChoice = input("Team Noughts: Enter the Row Letter and Column Number (E.G A2)\n")
    if noughtChoice == "A1" and a1 == " ":
        a1 = "0"
    if noughtChoice == "A2" and a2 == " ":
        a2 = "0"
    if noughtChoice == "A3" and a3 == " ":
        a3 = "0"
    if noughtChoice == "B1" and b1 == " ":
        b1 = "0" 
    if noughtChoice == "B2" and b2 == " ":
        b2 = "0"
    if noughtChoice == "B3" and b3 == " ":
        b3 = "0"
    if noughtChoice == "C1" and c1 == " ":
        c1 = "0"
    if noughtChoice == "C2" and c2 == " ":
        c2 = "0"
    if noughtChoice == "C3" and c3 == " ":
        c3 = "0"
    showBoard()

def checkBoard():
    global loop
    if a1 == "x" and a2 == "x" and a3 == "x":
        print("Crosses Win")
        loop = False
    if b1 == "x" and b2 == "x" and b3 == "x":
        print("Crosses Win")
        loop = False
    if c1 == "x" and c2 == "x" and c3 == "x":
        print("Crosses Win")
        loop = False
    if a1 == "x" and b1 == "x" and c1 == "x":
        print("Crosses Win")
        loop = False
    if a2 == "x" and b2 == "x" and c2 == "x":
        print("Crosses Win")
        loop = False
    if a3 == "x" and b3 == "x" and c3 == "x":
        print("Crosses Win")
        loop = False
    if a1 == "x" and b2 == "x" and c3 == "x":
        print("Crosses Win")
        loop = False
    if a3 == "x" and b2 == "x" and c1 == "x":
        print("Crosses Win")
        loop = False

    if a1 == "0" and a2 == "0" and a3 == "0":
        print("Noughts Win")
        loop = False
    if b1 == "0" and b2 == "0" and b3 == "0":
        print("Noughts Win")
        loop = False
    if c1 == "0" and c2 == "0" and c3 == "0":
        print("Noughts Win")
        loop = False
    if a1 == "0" and b1 == "0" and c1 == "0":
        print("Noughts Win")
        loop = False
    if a2 == "0" and b2 == "0" and c2 == "0":
        print("Noughts Win")
        loop = False
    if a3 == "0" and b3 == "0" and c3 == "0":
        print("Noughts Win")
        loop = False
    if a1 == "0" and b2 == "0" and c3 == "0":
        print("Noughts Win")
        loop = False
    if a3 == "0" and b2 == "0" and c1 == "0":
        print("Noughts Win")
        loop = False

def gameLoop():
    global count,loop
    while loop == True:
        checkBoard()
        if a1 != " " and a2 != " " and a3 != " " and b1 != " " and b2 != " " and b3 != " " and c1 != " " and c2 != " " and c3 != " " and loop != False #Checks if all spaces are filled
            print("All spaces filled: DRAW\n")
            loop=False
        elif loop != False:
            if count % 2 == 0: #Checks if count can be divided by 2 if so runs nought function
                noughtChoiceFunc()
            if count % 2 != 0:
                crossChoiceFunc() #Checks if count cant be divided by 2 if so runs cross function
        count+=1

showBoard()

gameLoop()