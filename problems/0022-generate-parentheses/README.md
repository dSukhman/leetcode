# 0022 — Generate Parentheses

Difficulty: Medium
Link: https://leetcode.com/problems/generate-parentheses/

## Approach

Use backtracking to generate all valid combinations of parentheses.

* Build the string step by step using recursion.
* Keep track of how many opening and closing parentheses have been used.
* Add an opening parenthesis if the number of opening parentheses is less than `n`.
* Add a closing parenthesis only if the number of closing parentheses is less than the number of opening parentheses.
* When the length of the string reaches `2 * n`, add it to the result list.
* Continue exploring all valid combinations recursively.

## Complexity

Time: O(4ⁿ / √n)
Space: O(n) — recursion depth

## Tags

String, Backtracking, Recursion
