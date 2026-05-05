# 0032 — Longest Valid Parentheses

Difficulty: Hard
Link: https://leetcode.com/problems/longest-valid-parentheses/

## Approach

Use a stack to track indices and compute lengths of valid parentheses.

* Initialize a stack with `-1` to handle edge cases.
* Iterate through the string:

  * If the current character is `'('`, push its index onto the stack.
  * If it is `')'`, pop from the stack.
* If the stack becomes empty, push the current index as a new base.
* Otherwise, calculate the length of the current valid substring using the difference between the current index and the top of the stack.
* Track the maximum length found.

This method efficiently keeps track of valid boundaries.

## Complexity

Time: O(n)
Space: O(n)

## Tags

String, Stack, Dynamic Programming
