"""
Problem: Valid Sudoku
Difficulty: Medium

Approach:
- Use three hash maps (defaultdict of sets) to track the numbers seen in each row, column, and 3x3 sub-box:
  - `rows`: Tracks numbers in each row.
  - `cols`: Tracks numbers in each column.
  - `squares`: Tracks numbers in each 3x3 sub-box, identified by a tuple `(r // 3, c // 3)`.
- Iterate through each cell in the 9x9 board:
  - If the cell is empty (contains '.'), skip it.
  - Check if the current number already exists in the corresponding row, column, or sub-box:
    - If it does, return `False` (the board is invalid).
  - Otherwise, add the number to the respective row, column, and sub-box sets.
- If no conflicts are found after processing all cells, return `True` (the board is valid).
"""
import collections

class Solution(object):
    def isValidSudoku(self, board):
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]) :
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True