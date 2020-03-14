#Text-Based Battleships
#An ide
import random
board = ["A1", "A2","A3","A4","A5","B1","B2","B3","B4","B5","C1","C2","C3","C4","C5","D1","D2","D3","D4","D5","E1","E2","E3","E4","E5"]

def playshipPositionSelect(board):
    for i in range(0,10):
        inputPos = raw_input("Please input a ship position.\n> ")
        if inputPos in board:
            if inputPos not in playshipos:
                playshipos.append(inputPos)
                print("Ship added to Board")
            else:
                print("You already have a ship there.")
        else:
            print("Position unavailable on board.")
    return playshipos

def aishipPositionSelect(board):
    for i in range(0,10):
        inputNum = random.randint(0,25)
        inputPos = board[inputNum]
        while inputPos not in playshipos:
            aishipos.append(inputPos)
        else:
            
    return aishipos

print("========================================")
print("========Welcome to Battleships!=========")
print("========================================")
oneortwo = int(input("Would you like to play with one, or two players?\n> "))
if oneortwo == 1:
    print("One player selected, ok")
    AI = True
    print("Player 1 please enter your ships starting positions.\n\n")
    player1shippos = playshipPositionSelect(board)
elif oneortwo == 2:
    print("Two player selected, ok")
    AI = False
    print("Player 1 please enter your ships starting positions.\n\n")
    player1shippos = playshipPositionSelect(board)
    print("Plaeyer 2 please enter your ships starting positions.\n\n")
    player2shippos = playshipPositionselect
else:
    oneortwo = int(input("Would you like to play with one or two players?(Enter 1 or 2)\n> "))
