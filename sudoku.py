#!/usr/bin/python3

"""
"""

def print_puzzle(grid):
    size = 9
    for i in range(size):
        for j in range(size):
            print(grid[i][j], end="|")
        print("\n------------------")
#end print_puzzle

def solve(grid, row, col, num):
    for x in range(9):
        if(grid[row][x] == num):
            return(False)
    
    for x in range(9):
        if(grid[x][col] == num):
            return(False)
    
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if(grid[i + start_row][j + start_col] == num):
                return(False)
    return(True)
#end of solve

def sudoku(grid, row, col):
    size = 9
    if(row == size-1 and col == size):
        return(True)
    
    if(col == size):
        row = row + 1
        col = 0
    
    if(grid[row][col] > 0):
        return(sudoku(grid, row, col+1))
    
    for num in range(1, size+1, 1):
        if(solve(grid, row, col, num)):
            grid[row][col] = num

            if(sudoku(grid, row, col+1)):
                return(True)
        grid[row][col] = 0
    
    return(False)
#end of sudoku

#end of sudoku

def main():
    debug = 1
    #grid will be 9x9
    #0 (zero) will be square to be solved

    grid = [
        [2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]
    ]

    print_puzzle(grid)

    if(sudoku(grid, 0, 0)):
        print("\n\n")
        print_puzzle(grid)
    else:
        print("no solution found")

#end of main

if __name__ == "__main__":
    main()
#end