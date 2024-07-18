def emptySpaceFinder(puzzle):
    for c in range(9):
        for r in range(9):
           if puzzle[c][r]==-1:
            return c,r
    return None,None

def isValid(puzzle,guess,row,col):
   rowValues=puzzle[row]
   if guess in rowValues:
      return False
   colValue=[]
   for i in range(9):
      colValue.append(puzzle[i][col])
   if guess in colValue:
      return False
   rowStart=(row//3)*3
   colStart=(col//3)*3
   for r in range(rowStart,rowStart+3):
      for c in range(colStart,colStart+3):
         if guess==puzzle[r][c]:
            return False
   return True


def solveSudoku(puzzle):
 row,col=emptySpaceFinder(puzzle)
 if row is None:
    return True
 

 for guess in range(1, 10):
        if isValid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solveSudoku(puzzle):
                return True
            puzzle[row][col] = -1
    
 return False

    

 


example_board = [
    [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
    [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
    [-1, -1, -1,   7, 1, 9,   -1, 8, -1],
    [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
    [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
    [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],
    [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
    [6, 7, -1,   1, -1, 5,   -1, 4, -1],
    [1, -1, 9,   -1, -1, -1,   2, -1, -1]
]

if solveSudoku(example_board):
    print("Sudoku solved successfully!")
else:
    print("No solution exists.")
print(example_board)