import json
def isPossible(pawn,where,game):
    fp,lp = pawn
    fw,lw = where
    if fp == "C" and fw == "B" or fp =="B" and fw == "A":
        if lp==lw and game[where]==" ":
            return 1
        elif int(lp)+1==int(lw) and game[where]=="O" or int(lp)-1==int(lw) and game[where]=="O":
            return 1
    return 0

def pawnExist(pawn,game):
    if game[pawn] == "H":
        return 1
    return 0
def pMove(pawn,where,game,player):
    if player == 0:
        pa = "H"
    else:
        pa = "O"
    game[where] = pa
    game[pawn] = " "

def isFinished(game):
    stuck = json.loads('{"A1":"O", "A2":" ", "A3":"O","B1":"H", "B2":"O", "B3":"H","C1":" ", "C2":"H", "C3":" "}')
    status = -1
    if game["A1"] == "H" or game["A2"] == "H" or game["A3"] == "H":
        status = 1
    if game["C1"] == "O" or game["C2"] == "O" or game["C3"] == "O":
        status = 0
    if game == stuck:
        status = 1
    # 1 ya3ni user won , 0 user khssr, -1 nothing happend
    return status
def gameOver(winner,game,msg):
    game = json.loads('{"A1":"O", "A2":"O", "A3":"O","B1":" ", "B2":" ", "B3":" ","C1":"H", "C2":"H", "C3":"H"}')
    if winner == 1:
        msg = "Congrats You have won !"
    else:
        msg = "Oh no! You lost to a computer u fucking noob!"
    return 0
def stuck(game):
    i = 0
    array = []
    for place in game :
        array.append(game[place])
        i= i+1
    for j in range(len(array)):
        if j+3 < len(array) and array[j] != " ":
            if array[j+3] != " ":
                print("blocked")

    return 0
