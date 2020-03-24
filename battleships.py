#Text-Based Battleships
#An idea
import random
import time
board = ["A1", "A2","A3","A4","A5","B1","B2","B3","B4","B5","C1","C2","C3","C4","C5","D1","D2","D3","D4","D5","E1","E2","E3","E4","E5"]
player1shippos = []
player2shippos = []
player1shots = []
player1hits = []
player2shots = []
player2hits = []

def bootDisplay(board):
    print ("\033[2J")
    print ("\033[u")
    print("========================================")
    print("========Welcome to Battleships!=========")
    print("========================================\n\n")
    print("The board:\n")
    print("",board[0], board[1], board[2], board[3], board[4], "\n", board[5], board[6], board[7], board[8], board[9], "\n", board[10], board[11], board[12], board[13], board[14], "\n", board[15], board[16], board[17], board[18], board[19], "\n", board[20], board[21], board[22], board[23], board[24], "\n\n\n")

def playshipPositionSelect(board):
    bootDisplay(board)
    x = 10
    playshipos = [] * 10
    for i in range(0,x):
        inputPos = input("Please input a ship position.\n> ")
        if inputPos not in playshipos:
            if inputPos in board:
                playshipos.append(inputPos)
                print("Ship added to Board\n")
                bootDisplay(board)
            else:
                print("Position not on board\n")
        else:
            print("You already have a ship there.\n")
            x+=1
    return playshipos

def aishipPositionSelect(board):
    x = 10
    aishipos = [] * 10
    for i in range(0,x):
        inputNum = random.randint(0,24)
        inputPos = board[inputNum]
        if inputPos not in aishipos:
            aishipos.append(inputPos)
        else:
            x+=1
    return aishipos

def playerTurn(board, curPlayPos, otherPlayPos, curPlayShots, curPlayHits):
    bootDisplay(board)
    print("Player's Hit Data")
    print("Position\tHit?")
    for i in range(0,len(curPlayShots)):
        print(curPlayShots[i], "\t", curPlayHits[i])
    print("Player's Ships")
    for i in range(0,len(curPlayPos)):
        print(curPlayPos[i], "\n")
    x=0
    for i in range(0,x):
        shotRound = input("Please enter your shot position.\n> ")
        if shotRound in board:
            if shotRound not in curPlayShots:
                if shotRound in otherPlayPos:
                    print("Hit!")
                    curPlayShots.append(shotRound)
                    otherPlayPos.pop(otherPlayPos.index(shotRound))
                    curPlayHits.append(True)
                else:                                                           #Illustrating that hoomans are stupid fucking twats since 14/03/2020 (Not the 3rd of February 2021, you stupid yanks)
                    print("Miss!")
                    curPlayShots.append(shotRound)
                    curPlayHits.append(False)
            else:
                print("You have already tried to hit that position.Try again.")
                x+=1
        else:
            print("Position isn't on the board.")
            x+=1
    print("Your turn is over.")
    return otherPlayPos, curPlayshots, curPlayHits


def aiTurn(board, playPos, aiShots, aiHits):
    x=0
    bootDisplay()
    for i in range(0,x):
        point = random.randint(0,25)
        aiShot = board[point]
        if aishot not in aiShots:                                               #Illustrating that robots aren't infallible since 2130, 24/03/2020 (I don't think this one needs any explanation, really.)
            if aiShot in playPos:
                print("Hit! at", aiShot)
                aiShots.append(aiShot)
                playPos.pop(playPos.index(aiShot))
                aiHits.append(True)
                time.sleep(3)
            else:
                print("Miss! at", aiShot)
                aiShots.append(aiShot)
                aiHits.append(False)
        else:
            x+=1
    return playPos, aishots, aiHits

print("\033[s")
bootDisplay(board)
oneortwo = int(input("Would you like to play with one, or two players?\n> "))
if oneortwo == 1:
    print("One player selected, ok")
    AI = True
    print("Player 1 please enter your ships starting positions.\n\n")
    player1shippos = playshipPositionSelect(board)
    player2shippos = aishipPositionSelect(board)
elif oneortwo == 2:
    print("Two player selected, ok")
    AI = False
    print("Player 1 please enter your ships starting positions.\n\n")
    player1shippos = playshipPositionSelect(board)
    bootDisplay(board)
    print("Player 2 please enter your ships starting positions.\n\n")
    player2shippos = playshipPositionSelect(board)
else:
    oneortwo = int(input("Would you like to play with one or two players?(Enter 1 or 2)\n> "))

bootDisplay(board)
if oneortwo == 1:
    print("Player's Turn")
    player2shippos, player1shots, player1hits = playerTurn(board, player1shippos, player2shippos, player1shots, player1hits)
    bootDisplay()
    print("AI's Turn")
    player1shippos, player2shots, player2hits = aiTurn(board, player1shippos, player2shots, player2hits)
else:
    print("Player 1's Turn")
    player2shippos, player1shots, player1hits = playerTurn(board, player1shippos, player2shippos, player1shots, player1hits)
    print("Player 2's Turn")
    player1shippos, player2shots, player2hits = playerTurn(board, player2shippos, player1shippos, player2shots, player2hits)
