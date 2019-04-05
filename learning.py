import json
import random
from mechanics import *
def getMoves():
    file1 = open("moves.txt","r")
    x = file1.readlines();
    file1.close()
    moves = []
    for row in x:
        # print(row)
        moves.append(json.loads(row))
    return moves
def getGames():
    file1 = open("games.txt","r")
    x = file1.readlines();
    file1.close()
    games = []
    for row in x:
        #print(row)
        games.append(json.loads(row))
    return games
def noMove(i):
    moves = getMoves()
    if moves[i] == []:
        return 1
    return 0
def aiMove(game):
    lastMove = []
    moves = getMoves()
    games = getGames()
    print(game)
    for i in range(len(games)):
        print(games[i])
        if game == games[i]:
            move = moves[i]
            ran = random.randrange(len(move))
            pMove(move[ran][0],move[ran][1],game,1)
            lastMove = [i,ran]
            print(lastMove)
            return lastMove
    return "NOPE"
def punish(lastMove):
    moves = getMoves()
    moves[lastMove[0]].remove(moves[lastMove[0]][lastMove[1]])
    #file1 = open("moves.txt","w")
    #for row in moves:
    #    x = file1.writelines(str(row)+"\n")
    #file1.close()
