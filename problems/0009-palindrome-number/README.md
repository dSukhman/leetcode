# 0009 — Palindrome Number

Difficulty: Easy
Link: https://leetcode.com/problems/palindrome-number/

## Approach

Reverse half of the number and compare it with the remaining half.

* Return False immediately if the number is negative or ends with zero (except zero itself).
* Reverse digits from the second half of the number.
* Continue until the reversed number is greater than or equal to the remaining number.
* Compare both halves to determine if the number is a palindrome.
* For odd-length numbers, remove the middle digit before comparison.

## Complexity

Time: O(log₁₀(n))
Space: O(1)

## Tags

Math, Integer
