import random

gameVar=(
    "S",
    "W",
    "G"
)
gamePointDic = {
    "S S":[0, 0],
    "S W":[1, 0],
    "S G":[0, 1],
    "W S":[0, 1],
    "W W":[0, 0],
    "W G":[1, 0],
    "G S":[1, 0],
    "G W":[0, 1],
    "G G":[0, 0],
}

def getRandom():
    random_number = random.randint(0, 2)
    return gameVar[random_number]


def getInput():
    counter =0
    while counter<3:
        x= input().upper()
        if x in gameVar:
            return x
        counter+= 1
        print("You have given invalid input given. you have ", 3-counter, " chance left")
    ValueError("stop")

def sayEacRoundWin(key, pointP, pointC):
    p = gamePointDic[key][0]
    c = gamePointDic[key][1]
    if (p < c):
        print("Computer choose ",key[-1], " computer Win and get a point\tP: ", pointP, "\tC: ", pointC)
    elif(p > c):
        print("Computer choose ",key[-1], " player Win and get a point\tP: ", pointP, "\tC: ", pointC)
    else:
        print("Computer choose ",key[-1], " Draw\tP: ", pointP, "\tC: ", pointC)


def checkQuit(inp):
    if (inp == 'Q'):
        finalCall = input("Are you Sure... Press Y to Quit an N to Continue").upper()
        if (inp == "Y"):
            exit()
        elif (inp != "N"):
            ValueError("Wrog input padh ke aao")



pointP = 0
pointC = 0

while (pointP < 5 and pointC < 5):
    gameVarC = getRandom()
    gameVarP = getInput()

    checkQuit(gameVarP)

    gameVarKey = gameVarP + " " + gameVarC
    
    pointC = pointC + gamePointDic[gameVarKey][1]
    pointP = pointP + gamePointDic[gameVarKey][0]

    sayEacRoundWin(gameVarKey, pointP, pointC)
print()


