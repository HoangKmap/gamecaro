import tkinter as tk 
import random 
bang = {1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '}
nguoichoi = 'O'
AI = 'X'

def printbang(bang):
        print(bang[1] + "|" + bang[2] + "|" + bang[3])
        print("-+-+-")
        print(bang[4] + "|" + bang[5] + "|" + bang[6])
        print("-+-+-")
        print(bang[7] + "|" + bang[8] + "|" + bang[9])
        print("\n")

def spaceIsFree(vitri):
    if bang[vitri] == ' ':
        return True 
    return False 

def insertLetter(letter, vitri):
    if spaceIsFree(vitri):
        bang[vitri] = letter 
        printbang(bang)
        if checkDraw():
            print("hoa")
            exit() 
        if checkWin():
            if letter == 'X':
                print("may tinh thang!")
                exit()
            else:
                print("nguoi choi thang!")
                exit()
        return 
    else:
        print("Invalid vitri")
        vitri = int(input("Hay chon vi tri di : "))
        insertLetter(letter, vitri)
        return    

def checkWin():
    if (bang[1] == bang[2] and bang[1] == bang[3] and bang[1] != ' '):
        return True
    elif (bang[4] == bang[5] and bang[4] == bang[6] and bang[4] != ' '):
        return True
    elif (bang[7] == bang[8] and bang[7] == bang[9] and bang[7] != ' '):
        return True
    elif (bang[1] == bang[4] and bang[1] == bang[7] and bang[1] != ' '):
        return True
    elif (bang[2] == bang[5] and bang[2] == bang[8] and bang[2] != ' '):
        return True
    elif (bang[3] == bang[6] and bang[3] == bang[9] and bang[3] != ' '):
        return True
    elif (bang[1] == bang[5] and bang[1] == bang[9] and bang[1] != ' '):
        return True
    elif (bang[7] == bang[5] and bang[7] == bang[3] and bang[7] != ' '):
        return True
    else:
        return False

def checkWhichMarkWon(mark):
    if (bang[1] == bang[2] and bang[1] == bang[3] and bang[1] == mark):
        return True
    elif (bang[4] == bang[5] and bang[4] == bang[6] and bang[4] == mark):
        return True
    elif (bang[7] == bang[8] and bang[7] == bang[9] and bang[7] == mark):
        return True
    elif (bang[1] == bang[4] and bang[1] == bang[7] and bang[1] == mark):
        return True
    elif (bang[2] == bang[5] and bang[2] == bang[8] and bang[2] == mark):
        return True
    elif (bang[3] == bang[6] and bang[3] == bang[9] and bang[3] == mark):
        return True
    elif (bang[1] == bang[5] and bang[1] == bang[9] and bang[1] == mark):
        return True
    elif (bang[7] == bang[5] and bang[7] == bang[3] and bang[7] == mark):
        return True
    else:
        return False

def checkDraw():
    for key in bang.keys():
        if bang[key] == ' ':
            return False 
    return True 

def nguoichoiMove():
    vitri = int(input("chọn vị trí đi cho 'O': "))
    insertLetter(nguoichoi, vitri)
    return 

def compMove():
    bestScore = -800
    bestMove = 0
    for key in bang.keys():
        if bang[key] == ' ':
            bang[key] = AI
            score = minimax(bang, False)
            bang[key] = ' '
            if score > bestScore:
                bestScore = score 
                bestMove = key
    insertLetter(AI, bestMove)
    return 
def minimax(bang, isMaximizing):
    if checkWhichMarkWon(AI):
        return 1 
    elif checkWhichMarkWon(nguoichoi):
        return -1 
    elif checkDraw():
        return 0
        
    if isMaximizing:
        bestScore = -800 
        for key in bang.keys():
            if bang[key] == ' ':
                bang[key] = AI 
                score = minimax(bang, False)
                bang[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore 
    else:
        bestScore = 800 
        for key in bang.keys():
            if bang[key] == ' ':
                bang[key] = nguoichoi 
                score = minimax(bang, True)
                bang[key] = ' '
                if score < bestScore:
                    bestScore = score 
        return bestScore


while not checkWin():
    compMove()
    nguoichoiMove()
