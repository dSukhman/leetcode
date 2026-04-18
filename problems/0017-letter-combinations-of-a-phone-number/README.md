# 0017 — Letter Combinations of a Phone Number

Difficulty: Medium
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

## Approach

Use backtracking to generate all possible letter combinations for the given digits.

* Create a mapping of digits to their corresponding letters.
* Use recursion (backtracking) to build combinations one digit at a time.
* For each digit, iterate through its possible letters.
* Append each letter to the current combination and move to the next digit.
* When the combination length equals the number of digits, add it to the result list.
* Return all generated combinations.

## Complexity

Time: O(4ⁿ) — each digit can map to up to 4 letters
Space: O(n) — recursion depth

## Tags

String, Backtracking, Recursion
