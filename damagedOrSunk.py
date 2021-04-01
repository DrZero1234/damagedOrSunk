# damagedOrSunk.py - In a game of battleship registers if the attack missed,damaged or sunk a ship

"""
Your task in the kata is to determine how many boats are sunk damaged and untouched from a set amount of attacks.
 You will need to create a function that takes two arguments, the playing board and the attacks.

 KATA Link - https://www.codewars.com/kata/58d06bfbc43d20767e000074/train/python
"""

import numpy as np


def damaged_or_sunk(board, attacks):
    # Flipped the table upside down since in the task the row indexing is reversed
    npBoard = np.array(board)
    board = np.flipud(npBoard)

    print(board)
    # Setting up the dictionary with the needed keys, the default value for these keys are 0.
    dictionaryKeys = ['sunk', 'damaged', 'not_touched', 'points']
    resultDictionary = {}
    for key in dictionaryKeys:
        resultDictionary.setdefault(key, 0)
    # Getting all the unique values (except 0) from the board for the not_touched later
    touchCheckList = []
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] != 0 and board[x][y] not in touchCheckList:
                touchCheckList.append(board[x][y])
    touched = []
    damaged = []
    # Iterating through the attacks
    for attack in attacks:
        # Setting up the correct indexes for the attacks
        attackCol = attack[0] - 1
        attackRow = attack[1] - 1
        currentAttack = board[attackRow][attackCol]
        # IF the attack hits the field will be replaced with 0
        if currentAttack != 0:
            board[attackRow][attackCol] = 0
            # Checks if the Ship is still in the board and the ship´s number in the list damaged
            if currentAttack in board and currentAttack not in damaged:
                # If the ship  got its first hit the ship´s number will be added to the list damaged and will be counted as damaged in the dicitonary
                damaged.append(currentAttack)
                resultDictionary['damaged'] += 1
                touched.append(currentAttack)
            # If the ship is not in the board anymore it means it sunk so the dictionary sunk key will be increased by 1
            elif currentAttack not in board:
                resultDictionary['sunk'] += 1
                # Check if the ship´s been damaged if yes then the damaged key will be decreased by 1 because the ship is sunk not damaged
                if resultDictionary['damaged'] >= 1:
                    resultDictionary['damaged'] -= 1
                touched.append(currentAttack)
    for shipNum in touchCheckList:
        # The touched list kept track on the ships that has been hit, if there is a ship number which is not in the touched list the not_touched key will be increased by 1
        if shipNum not in touched:
            resultDictionary['not_touched'] += 1
    # Calculating the result
    resultDictionary['points'] = ((resultDictionary['sunk'] * 1) + (
        resultDictionary['damaged'] * 0.5)) - (resultDictionary['not_touched'] * 1)
    return resultDictionary


# SOME BASIC TEST CASES FROM THE KATA WEBSITE

print(damaged_or_sunk([[0, 0, 0, 2, 2, 0],
                       [0, 3, 0, 0, 0, 0],
                       [0, 3, 0, 1, 0, 0],
                       [0, 3, 0, 1, 0, 0]], [[2, 1], [1, 3], [4, 2]]))


print(damaged_or_sunk([[0, 0, 1, 0],
                       [0, 0, 1, 0],
                       [0, 0, 1, 0]], [[3, 1], [3, 2], [3, 3]]))


print(damaged_or_sunk([[3, 0, 1],
                       [3, 0, 1],
                       [0, 2, 1],
                       [0, 2, 0]], [[2, 1], [2, 2], [3, 2], [3, 3]]))
