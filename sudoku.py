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

def sudoku(grid, row, col):
    pass

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

#end of main

if __name__ == "__main__":
    main()
#end