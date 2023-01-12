# Prof. K
# DS 510
# Assignment 10 Part A - Numpy multi-dimension arrays

import numpy as np
from numpy import random

if __name__ == "__main__":
    names=['Ann','Bob','Cindy-Lou-Who','Dan','Edie','Frank','Gigi','Hank','Ina','Jim','Kim','Len','Mimi','Nick','Olivia']
    lenLongestName = len(max(names,key=len))
    rows = int(input('Enter the numbers of rows: '))
    chairs = int(input('Enter the numbers of chairs per row: '))
    print()

    # start with a 1-D Numpy array
    desks = np.array( [] )

    # randomly fill names into the array, as strings centered in
    # a field that is as long as the longest name
    for i in range(0,rows):
        for j in range(0,chairs):
            randName = random.choice(names)
            tempStr = f'{randName:^{lenLongestName}}'
            desks = np.append(desks,tempStr)
            names.remove(randName)
    
    # reshape the desks array to be 2-D, rows by cols
    desks = desks.reshape(rows,chairs)
    
    # print a row of names at a time
    # directly underneath print the ( row , col ) coord
    for i in range(0,rows):
        for j in range(0,chairs):
            print(desks[i][j], end=' ')
        print()
        for j in range(0,chairs):
            tempStr='('+str(i)+','+str(j)+')'
            print(f'{tempStr:^{lenLongestName}}',end=' ')
        print('\n')