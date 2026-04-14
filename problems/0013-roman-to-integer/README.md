# 0013 — Roman to Integer

Difficulty: Easy
Link: https://leetcode.com/problems/roman-to-integer/

## Approach

Use a hash map to store Roman numeral values.

* Traverse the string from left to right.
* Compare the current numeral with the next numeral.
* If the current value is smaller than the next value, subtract it from the result.
* Otherwise, add the current value to the result.
* Continue until all characters are processed.

## Complexity

Time: O(n)
Space: O(1)

## Tags

Hash Table, Math, String
