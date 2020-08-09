import time
import random
import subprocess

board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]
print('Welcome to Tic-Tac-Toe')
global Xturn
Xturn = random.randint(0, 1)


def print_board(bo):
    print("                                            ")
    print("  |   |")
    print(bo[0], "|", bo[1], "|", bo[2])
    print("  |   |")
    print('--|---|---')
    print("  |   |")
    print(bo[3], "|", bo[4], "|", bo[5])
    print("  |   |")
    print('--|---|---')
    print("  |   |")
    print(bo[6], "|", bo[7], "|", bo[8])
    print("  |   |")
    print('\n')
    print('===================================================================')
    print('\n')

print_board(board)

def wintry(bo, le):
    if bo[0] == le and bo[1] == le and bo[2] == le or \
            bo[3] == le and bo[4] == le and bo[5] == le or \
            bo[6] == le and bo[7] == le and bo[8] == le or \
            bo[0] == le and bo[3] == le and bo[6] == le or \
            bo[1] == le and bo[4] == le and bo[7] == le or \
            bo[2] == le and bo[5] == le and bo[8] == le or \
            bo[0] == le and bo[4] == le and bo[8] == le or \
            bo[2] == le and bo[4] == le and bo[6] == le:
        return True

def win(bo, le):
    if bo[0] == le and bo[1] == le and bo[2] == le or \
            bo[3] == le and bo[4] == le and bo[5] == le or \
            bo[6] == le and bo[7] == le and bo[8] == le or \
            bo[0] == le and bo[3] == le and bo[6] == le or \
            bo[1] == le and bo[4] == le and bo[7] == le or \
            bo[2] == le and bo[5] == le and bo[8] == le or \
            bo[0] == le and bo[4] == le and bo[8] == le or \
            bo[2] == le and bo[4] == le and bo[6] == le:
        if le == "X":
            print('X won good job!!')
            time.sleep(5)
            board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            print_board(bo)            
            Xmove(board)
            print('\n \n Welcome to Tic-Tac-Toe')

        if le == "O":
            print('O won, good job!!')
            time.sleep(5)
            board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            print_board(bo)            
            Xmove(board)
            print('\n \n Welcome to Tic-Tac-Toe')
    else:
        return False



def tie(bo, le):
    tienum = 0
    for x in range(0, 9):
        if bo[x] == " ":
            pass
        else:
            tienum = tienum + 1
        if tienum == 9 and win(bo, le) == False:
            print("Tie!")
        else:
            pass

def checkplace(bo, choice, le):
    if choice >= 0 and choice <= 8:
        if bo[choice] == " ":
            bo[choice] = le
            print_board(bo)
            win(bo, le)
            tie(bo, le)
            return True
        else:
            print('Sorry that space is full')
            time.sleep(1.5)
            return False
    else:
        print('You have to insert a number from 1 to 9')
        return False

def X(bo):
    choice = input("X turn, a number from 1 to 9: ")
    choice = int(choice)
    choice = choice - 1
    if checkplace(bo, choice, "X"):
        O(bo)
    else:
        X(bo)


def O(bo):
    possmoves = [x for x, letter in enumerate(bo) if letter == " "]
    for letter in ['O', 'X']:
        for x in possmoves:
            copyboard = board[:]
            copyboard[x] = letter
            if wintry(copyboard, letter):
                choice = x
                checkplace(bo, choice, 'O')
                X(bo)
    for y in possmoves:
        for x in [0, 2, 6, 8]:
            if y == x:
                checkplace(bo, x, 'O')
                X(bo)
    for x in possmoves:
        if x == 4:
            checkplace(bo, x, 'O')
            X(bo)
    if possmoves != 0:
        choice = random.choice(possmoves)
        checkplace(bo, choice, 'O')
        X(bo)









def Xmove(bo):
    win(bo, "X")
    win(bo, "O")
    tie(bo, "X")
    tie(bo, "O")
    global Xturn
    if Xturn == 1:
        Xturn = 0
        X(bo)
    else:
        Xturn = 1
        O(bo)


Xmove(board)
