# 0010 — Regular Expression Matching

Difficulty: Hard
Link: https://leetcode.com/problems/regular-expression-matching/

## Approach

Use recursion with memoization to simulate regex matching.

* Define a recursive function to compare characters from the string and pattern.
* If the pattern is exhausted, the string must also be exhausted.
* Check if the current characters match (including the `.` wildcard).
* If the next pattern character is `*`, either skip the pattern or use it if characters match.
* Use memoization to store previously computed results and avoid recomputation.
* Return whether the entire string matches the pattern.

## Complexity

Time: O(m × n)
Space: O(m × n)

## Tags

String, Dynamic Programming, Recursion
