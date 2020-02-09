import numpy as np
import sys
from colorama import Fore, Back, Style
from bcolors import bcolors

SIZE=20
threshold=50  #treschold
ratio=0.5

map = np.zeros((SIZE, SIZE), dtype='int')

def printMap(map):
    print('')
    print('=======================================')
    for i in range(len(map)):
        for j in range(len(map[0])):
            if (map[i, j] == 0):
                print(str(map[i, j]), end=" ")
            elif (map[i, j] == 1):
                print(bcolors.BLUE + str(map[i, j]) + bcolors.WHITE, end=" ")
            else:
                print(bcolors.RED + str(map[i, j]) + bcolors.WHITE, end=" ")
        print('')
    print(Fore.WHITE)

def satisfiability(map, x, y):
    num_similar=0
    type = map[x, y]
    if (type == 0):
        return -1
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if ((i != x or j != y) and (i >= 0 and j >= 0 and i<= SIZE-1 and j<=SIZE-1)):
                if (map[i, j] == type):
                    num_similar += 1
    if ((x == 0 and y == 0) or (x == 0 and y == SIZE-1) or (x == SIZE-1 and y == 0) or (x == SIZE-1 and y == SIZE-1)):
        return (num_similar / 3) * 100
    elif (x > 0 and x < SIZE-1 and y > 0 and y < SIZE-1):
        return (num_similar / 8) * 100
    else:
        return (num_similar / 5) * 100

def findEmptySpace(map):
    flag=False
    while(not flag):
        x = np.random.randint(len(map))
        y = np.random.randint(len(map[0]))
        if (map[x, y] == 0):
            return (x, y)

try:
    ratio = float(sys.argv[2])
except:
    pass
finally:
    #Place Population 1 in the map
    for i in range(int(250*ratio)):
        flag=False
        while(not flag):
            x = np.random.randint(SIZE)
            y = np.random.randint(SIZE)
            if (map[x, y] == 0):
                map[x, y] = 1
                flag=True

    #Place Population 2 in the map
    for i in range(int(250*(1-ratio))):
        flag=False
        while(not flag):
            x = np.random.randint(SIZE)
            y = np.random.randint(SIZE)
            if (map[x, y] == 0):
                map[x, y] = 2
                flag=True

#main
try:
    threshold = float(sys.argv[1])
except:
    print("""
    usage: python3 schelling.py [t] [ratio]

    t     in [0, 100]             : the tolerance threshold
    ratio in ]0, 1[ (default 0.5) : the proportion of the first population

    """)
else:
    printMap(map)
    print("The execution will stop if there is no more migrations\n")
    input("Press any key to start")

    while(True):
        num_switches = 0
        for i in range(len(map)):
            for j in range(len(map[0])):
                if (map[i, j] != 0 and satisfiability(map, i, j) < threshold):
                    (x, y) = findEmptySpace(map)
                    type = map[i, j]
                    map[i, j] = 0
                    map[x, y] = type
                    num_switches += 1
        printMap(map)
        if (num_switches == 0):
            break
