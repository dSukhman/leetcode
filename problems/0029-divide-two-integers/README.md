# 0029 — Divide Two Integers

Difficulty: Medium
Link: https://leetcode.com/problems/divide-two-integers/

## Approach

Use bit manipulation and repeated subtraction to simulate division.

* Handle the overflow edge case when dividing `-2³¹` by `-1`.
* Determine the sign of the result based on the inputs.
* Convert both numbers to positive values.
* Repeatedly subtract the largest multiple of the divisor from the dividend.
* Use bit shifting to find the largest multiple (`divisor << k`).
* Accumulate the result using powers of two.
* Apply the correct sign to the final result.

This avoids using multiplication, division, or modulo operators.

## Complexity

Time: O(log n)
Space: O(1)

## Tags

Math, Bit Manipulation
