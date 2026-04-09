# 0006 — Zigzag Conversion

Difficulty: Medium
Link: https://leetcode.com/problems/zigzag-conversion/

## Approach

Simulate writing characters in a zigzag pattern using rows.

Create a list to store strings for each row:

* Traverse the input string character by character.
* Append each character to the current row.
* Change direction when reaching the first or last row.
* Move up or down between rows accordingly.
* After processing all characters, join all rows to form the final string.

Handle edge cases where the number of rows is 1 or greater than the string length.

## Complexity

Time: O(n)
Space: O(n)

## Tags

String, Simulation
