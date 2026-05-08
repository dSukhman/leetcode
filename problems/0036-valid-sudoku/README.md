# 0036 — Valid Sudoku

Difficulty: Medium
Link: https://leetcode.com/problems/valid-sudoku/

## Approach

Use hash sets to track seen values in rows, columns, and 3×3 sub-boxes.

* Create:

  * A hashmap of sets for rows
  * A hashmap of sets for columns
  * A hashmap of sets for 3×3 boxes
* Traverse every cell in the board.
* Skip empty cells (`"."`).
* Before inserting a number:

  * Check if it already exists in the current row.
  * Check if it already exists in the current column.
  * Check if it already exists in the corresponding 3×3 box.
* If a duplicate is found, return `False`.
* Otherwise, insert the value into the appropriate sets.
* Return `True` if the board is valid.

## Complexity

Time: O(1)

* The board size is fixed at 9×9

Space: O(1)

## Tags

Array, Hash Set, Matrix
