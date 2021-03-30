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
    print(touchCheckList)
    touched = []
    # Iterating through the attacks
    for attack in attacks:
        # Setting up the correct indexes for the attacks
        attackCol = attack[0] - 1
        attackRow = attack[1] - 1
        currentAttack = board[attackRow][attackCol]
        #
        if currentAttack != 0:
            board[attackRow][attackCol] = 0
            if currentAttack in board:
                resultDictionary['damaged'] += 1
                touched.append(currentAttack)
            else:
                resultDictionary['sunk'] += 1
                resultDictionary['damaged'] = 0
                touched.append(currentAttack)
    for uniqueNumber in touchCheckList:
        if uniqueNumber not in touched:
            resultDictionary['not_touched'] += 1
    resultDictionary['points'] = int(((resultDictionary['sunk'] * 1) + (
        resultDictionary['damaged'] * 0.5)) - (resultDictionary['not_touched'] * 1))
    return resultDictionary


print(damaged_or_sunk([[0, 0, 0, 2, 2, 0],
                       [0, 3, 0, 0, 0, 0],
                       [0, 3, 0, 1, 0, 0],
                       [0, 3, 0, 1, 0, 0]], [[2, 1], [1, 3], [4, 2]]))
