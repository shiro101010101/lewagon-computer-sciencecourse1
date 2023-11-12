# pylint: disable=missing-docstring
# i = row
# j = col
# grid[i][j]


#check 9row
def isRowValid(grid[i]):
    return len(set(grid[i])) == 9

#check 9column
def isColValid(grid[j]):
    col = [item[grid[j]] for item in grid]
    return len(set(col)) == 9

#validate cell
def isCelValid(grid[i], grid[j]):
    vals = grid[cel_row][cel_col: cel_col+3]
    vals.extend(grid[cel_row+1] [cel_col: cel_col+3])
    vals.extend(grid[cel_row+2] [cel_col: cel_col+3])
    return len(set(vals)) == 9

#validate grid
def validategrid():
    for i in range(0,9):
        if not isRowValid(i):
            return False
        if not isColValid(i):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            print(i, j)
            if not isCelValid(i, j):
                return False
    return True

grid = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9,1],
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,8]]

if validateSudoku():
    print("Sudoku is valid.")
else:
    print("Sudoku is not valid.")

def sudoku_validator(grid):
