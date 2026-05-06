# 0034 — Find First and Last Position of Element in Sorted Array

Difficulty: Medium
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

## Approach

Use binary search twice to find the first and last occurrence of the target.

* Create a helper binary search function.
* When the target is found:

  * Continue searching left to find the first occurrence.
  * Continue searching right to find the last occurrence.
* Perform:

  * One search for the left boundary.
  * One search for the right boundary.
* Return both indices.

This keeps the overall runtime logarithmic.

## Complexity

Time: O(log n)
Space: O(1)

## Tags

Array, Binary Search
