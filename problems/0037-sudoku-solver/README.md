# 0037 — Sudoku Solver

Difficulty: Hard
Link: https://leetcode.com/problems/sudoku-solver/

## Approach

Use backtracking to fill empty cells while maintaining Sudoku validity.

* Traverse the board to find an empty cell (`"."`).
* Try placing digits `'1'` through `'9'`.
* For each digit:

  * Check if placing it is valid:

    * No duplicates in the row
    * No duplicates in the column
    * No duplicates in the 3×3 sub-box
* If valid:

  * Place the digit
  * Recursively continue solving the board
* If the recursive call fails:

  * Undo the placement (backtrack)
* If all cells are filled successfully, return `True`.

The board is modified in-place.

## Complexity

Time: Exponential (backtracking search)
Space: O(1) excluding recursion stack

## Tags

Backtracking, Matrix, Recursion
