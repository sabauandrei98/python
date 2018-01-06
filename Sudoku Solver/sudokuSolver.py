from copy import deepcopy

sudokuTable = [[0,0,0,0,2,0,9,0,0],
               [0,0,0,0,0,7,3,5,1],
               [5,0,7,0,0,0,0,0,0],
               [0,8,0,0,0,0,0,0,5],
               [7,0,0,0,0,9,0,0,0],
               [0,0,0,0,1,0,0,2,8],
               [0,0,3,0,9,5,0,4,6],
               [0,6,0,3,0,0,0,0,0],
               [9,5,4,0,0,0,0,1,0]]

def isFull(sudoku):
    for i in range(0, 9):
        for j in range (0, 9):
            if sudoku[i][j] == 0:
                return False
    return True

def isGoodMatrix(sudoku):
    for i in range(0, 9):
        for j in range (0, 9):
            if not goodNumber(i,j,sudoku):
                return False
    return True

def goodNumber(l, c, sudoku):
    freq = [0,0,0,0,0,0,0,0,0,0]
    for ii in range(int(l/3) * 3, int(l/3) * 3 + 3):
        for jj in range(int(c/3) * 3, int(c/3) * 3 + 3):
            if sudoku[ii][jj] != 0:
                freq[sudoku[ii][jj]] += 1
                if freq[sudoku[ii][jj]] == 2:
                    return False

    freqL = [0,0,0,0,0,0,0,0,0,0]
    freqC = [0,0,0,0,0,0,0,0,0,0]

    for i in range(0, 9):
        if sudoku[l][i] != 0:
            freqL[sudoku[l][i]] += 1
            if freqL[sudoku[l][i]] == 2:
                return False

        if sudoku[i][c] != 0:
            freqC[sudoku[i][c]] += 1
            if freqC[sudoku[i][c]] == 2:
                return False

    return True

def printSolution(sudoku):
    for x in sudoku:
        print (x)
    print('\n\n\n')
    input("Done!")

def sudokuSolver(sudoku):
    if not isFull(sudoku):
        for i in range(0, 9):
            for j in range(0, 9):
                if sudoku[i][j] == 0:
                    l = deepcopy(sudoku)
                    for k in range(1, 10):
                        l[i][j] = k
                        if goodNumber(i,j,l):
                            sudokuSolver(l)
                        else:
                            l[i][j] = 0
                if sudoku[i][j] == 0:
                    return
    elif isGoodMatrix(sudoku):
        printSolution(sudoku)


if isGoodMatrix(sudokuTable):
    print("Solving matrix..")
    sudokuSolver(sudokuTable)
else:
    print("Wrong matrix !")