# 0012 — Integer to Roman

Difficulty: Medium
Link: https://leetcode.com/problems/integer-to-roman/

## Approach

Use a greedy approach with predefined Roman numeral values.

* Create a list of integer values paired with their Roman numeral symbols.
* Iterate through the list from largest to smallest value.
* While the number is greater than or equal to the current value, append the corresponding symbol and subtract the value.
* Continue until the number becomes zero.
* Join all collected symbols to form the final Roman numeral string.

## Complexity

Time: O(1)
Space: O(1)

## Tags

Math, String, Greedy
