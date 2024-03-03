# -*- coding: utf-8 -*-
"""
Created on Wed May 10 14:33:11 2023

@author: divya, kartheek
"""

import random

def print_board(board):
    '''Prints the board'''
    boardString = ""
    for i in range(9):
        for j in range(9):
            boardString += str(board[i][j]) + " "
            if (j+1)%3 == 0 and j != 0 and (j+1) != 9:
                boardString += "| "

            if j == 8:
                boardString += "\n"

            if j == 8 and (i+1)%3 == 0 and (i+1) != 9:
                boardString += "- - - - - - - - - - - \n"
    print(boardString)

def find_empty(board):
    '''Finds an empty cell and returns its position as a tuple'''
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j

def valid(board, pos, num):
    '''Whether a number is valid in that cell, returns a bool'''
    for i in range(9):
        if board[i][pos[1]] == num and (i, pos[1]) != pos:  # make sure it isn't the same number we're checking for by comparing coords
            return False

    for j in range(9):
        if board[pos[0]][j] == num and (pos[0], j) != pos:  # Same row but not same number
            return False

    start_i = pos[0] - pos[0] % 3  # ex. 5-5%3 = 3 and thats where the grid starts
    start_j = pos[1] - pos[1] % 3
    for i in range(3):
        for j in range(3):  # adds i and j as needed to go from start of grid to where we need to be
            if board[start_i + i][start_j + j] == num and (start_i + i, start_j + j) != pos:
                return False
    return True

def generate_board(difficulty):
    '''Generates a Sudoku board with the specified difficulty level'''
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve(board)  # Solve a fully filled board

    # Remove cells based on difficulty level
    cells_to_remove = 0
    if difficulty == "easy":
        cells_to_remove = random.randint(30, 40)
    elif difficulty == "medium":
        cells_to_remove = random.randint(40, 50)
    elif difficulty == "hard":
        cells_to_remove = random.randint(50, 60)

    while cells_to_remove > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            cells_to_remove -= 1

    return board

def solve(board):
    '''Solves the Sudoku board via the backtracking algorithm'''
    empty = find_empty(board)
    if not empty:  # no empty spots are left so the board is solved
        return True

    for nums in range(9):
        if valid(board, empty, nums+1):
            board[empty[0]][empty[1]] = nums+1

            if solve(board):  # recursive step
                return True
            board[empty[0]][empty[1]] = 0  # this number is wrong so we set it back to 0
    return False

if __name__ == '__main__':
    difficulty = input("Choose difficulty level (easy, medium, hard): ")
    board = generate_board(difficulty.lower())

    print("Generated Sudoku Board:")
    print_board(board)

    solve(board)

    print("\nSolved Sudoku Board:")
    print_board(board)