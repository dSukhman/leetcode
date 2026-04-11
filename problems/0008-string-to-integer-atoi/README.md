# 0008 — String to Integer (atoi)

Difficulty: Medium
Link: https://leetcode.com/problems/string-to-integer-atoi/

## Approach

Simulate the conversion process step by step.

* Remove leading whitespace from the string.
* Check for an optional sign (`+` or `-`) and set the sign accordingly.
* Iterate through the digits and build the integer value.
* Stop when a non-digit character is encountered.
* Clamp the result within the 32-bit signed integer range.
* Return the final value with the correct sign.

## Complexity

Time: O(n)
Space: O(1)

## Tags

String, Simulation
