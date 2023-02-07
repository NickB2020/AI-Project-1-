#Artificial Intelligence 010
#Nick Bischoff, nbb12
#Project 1
#This Program is a N-queens solution, written in python.
#This program utilizes backtracking using recursion using a 2-dimensional list.
#This program reads in the values for the board from an "input.csv" file.
#Then calculates if there is a solution, if there is, then it outputs the solution
#to the "solution.csv" file. If there is no solution possible, then the Program
#prints to console "no solution" and does not update the "solution.csv" file.

#pre: Input file needs to be read in order to get the board starting position
#post: Now we can check the row and column for a spot.
# return True for position in range
#        False for position out of range
def isValid(n, row, col):
    return row >= 0 and row < n and col >= 0 and col < n

#pre: Input file needs to be read in order to get the board starting position
#post: Now we can check the row for a spot
# return True, if in row only 1 one is present
#        False, otherwise
def validRow(board, n, row):
    # count is used for counting the queens
    count = 0
    for col in range(n):
        # queen found
        if board[row][col] == 1:
            count += 1

        # queens > 1
        if count > 1:
            return False

    return True

#pre: Input file needs to be read in order to get the board starting position
#post: Now we can check the column for a spot
# return True, if in column-col only 1 one is present
#        False, otherwise
def validCol(board, n, col):
    # count is used for counting the queens
    count = 0
    for row in range(n):
        # queen found
        if board[row][col] == 1:
            count += 1

        # queens > 1
        if count > 1:
            return False

    return True

#pre: Input file needs to be read in order to get the board starting position
#post: Now we can check the first diagonal for a spot
# return True, if in main diagonal going with (row, col) only 1-one is present
#        False, otherwise
# assume, in (row, col): 1 is present already
def validMainDiag(board, n, row, col):
    r, c = row+1, col+1
    while isValid(n, r, c):
        # Queen other than (row, col) found
        if board[r][c] == 1:
            return False
        r += 1
        c += 1

    r, c = row-1, col-1
    while isValid(n, r, c):
        # Queen other than (row, col) found
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    return True

#pre: Input file needs to be read in order to get the board starting position
#post: Now we can check the second diagonal for a spot
# return True, if in Secondary diagonal going with (row, col) only 1-one is present
#        False, otherwise
# assumption: in (row, col): 1 is present already
def validSecondaryDiag(board, n, row, col):
    r, c = row+1, col-1
    while isValid(n, r, c):
        # Queen other than (row, col) found
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1

    r, c = row-1, col+1
    while isValid(n, r, c):
        # Queen other than (row, col) found
        if board[r][c] == 1:
            return False
        r -= 1
        c += 1

    return True

#pre: Input file must be read, all other validations must be made
#post: This is a final check to make sure the placement is good
# return True, if placement of 1 at (row, col) is Valid
#        False, otherwise
def isValidPlacement(board, n, row, col):
    return (
        validCol(board, n, col) and
        validMainDiag(board, n, row, col) and
        validSecondaryDiag(board, n, row, col)
    )

# return True, if queen is already present in row
#        False, otherwise
def queenPresentOrNot(board, n, row):
    for col in range(n):
        if board[row][col] == 1:
            return True

    return False

#pre: All validations must be made
#post: Now we can use backtracking to find a solution or not
# solve n-queen problem recursively
def solveNQueen(board, n, row):
    # if board is finised, means board is solved successfully, so return True
    if row == n:
        return True

    # check for queen presence in row
    # assumption: already placed queen must be in correct position
    if queenPresentOrNot(board, n, row) == True:
        return solveNQueen(board, n, row+1)


    # check for each col from 0 to n-1
    for col in range(n):
        # place queen for testing
        board[row][col] = 1
        # if placement is correct and rest of the board solved successfully
        if isValidPlacement(board, n, row, col) and solveNQueen(board, n, row+1):
            return True

        # if board not solved with placing queen in (row, col)
        # then remove the queen from (row, col)
        board[row][col] = 0

    # this state failed to solve, so return False
    return False

# declare empty list
board = []
# open 'input.csv'
with open('input.csv', 'r') as file:
    # read 1 line
    line = file.readline()
    # if line have some data
    while line:
        # convert the line in interger list
        # then append the integer list to board
        board.append(list(map(int, line.strip().split(','))))
        # read another line
        line = file.readline()

# find number of columns in board
n = len(board[0])

# solve the N-queen proble
if solveNQueen(board, n, 0) == False:
    # if no solution found
    print('No solution')

else:
    # if solution found
    # open 'Solution.csv' in write mode
    with open('solution.csv', 'w') as file:
        # run loop for each row of board
        for row in board:
            # create line by joining each element of row separated by ','
            line = ','.join(map(str, row)) + '\n'
            # write line in file
            file.write(line)

    # print(Solution Found Successfully)
    print('Solution Saved Successfully')
