from learning import *
from mechanics import *
import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
b=1
game = json.loads('{"A1":"O", "A2":"O", "A3":"O","B1":" ", "B2":" ", "B3":" ","C1":"H", "C2":"H", "C3":"H"}')
placeholders = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
msg = "BITCH PLAAAY"
while b==1:
    clear()
    stuck(game);
    print(msg)
    print(" ---1--|---2--|---3--")
    print("A   "+game['A1']+"  |   "+game['A2']+"  |   "+game['A3']+"  ")
    print("       |      |      ")
    print(" ------|------|------")
    print("B   "+game['B1']+"  |   "+game['B2']+"  |   "+game['B3']+"  ")
    print("       |      |      ")
    print(" ------|------|------")
    print("C   "+game['C1']+"  |   "+game['C2']+"  |   "+game['C3']+"  ")
    print("       |      |      ")
    pawn = raw_input("Which pawn to move : ")
    where = raw_input("Where to move it : ")
    if pawn in placeholders and where in placeholders:
        isPossible(pawn,where,game)
        pawnExist(pawn,game)
        if isPossible(pawn,where,game) and pawnExist(pawn,game):
            pMove(pawn,where,game,0)
            isf = isFinished(game)
            if isf !=-1:
                game = json.loads('{"A1":"O", "A2":"O", "A3":"O","B1":" ", "B2":" ", "B3":" ","C1":"H", "C2":"H", "C3":"H"}')
                if isf == 1:

                    msg = "Congrats You have won !"
                    punish(lastMove)

                else:
                    msg = "Oh no! You lost to a computer u fucking noob!"
                continue
            lastMove = aiMove(game)
            isf = isFinished(game)
            if isf !=-1:
                game = json.loads('{"A1":"O", "A2":"O", "A3":"O","B1":" ", "B2":" ", "B3":" ","C1":"H", "C2":"H", "C3":"H"}')
                if isf == 1:
                    msg = "Congrats You have won !"
                    punish(lastMove)
                else:
                    msg = "Oh no! You lost to a computer u fucking noob!"

            msg = "BITCH PLAAAY"
        else:
            msg ="Your move is illogical arass lbota"
    else:
        msg = "Either ur pawn or target placeholder do not exist !"
