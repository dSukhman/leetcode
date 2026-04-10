# 0007 — Reverse Integer

Difficulty: Medium
Link: https://leetcode.com/problems/reverse-integer/

## Approach

Reverse the integer digit by digit.

Handle the sign separately:

* Determine the sign of the number and convert it to positive.
* Extract digits using modulo (`% 10`) and build the reversed number.
* Before adding each digit, check if the result would overflow the 32-bit signed integer range.
* Return 0 if overflow would occur.
* Restore the original sign before returning the result.

## Complexity

Time: O(log₁₀(n))
Space: O(1)

## Tags

Math, Integer
