# 0004 — Median of Two Sorted Arrays

Difficulty: Hard
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

## Approach

Use binary search to partition the smaller array.

Partition both arrays so:

* Left partitions contain half of the elements.
* All elements in the left partitions are less than or equal to those in the right partitions.
* Handle edge cases using negative and positive infinity.
* Once the correct partition is found, compute the median based on whether the total length is even or odd.

## Complexity

Time: O(log(min(m, n)))
Space: O(1)

## Tags

Array, Binary Search, Divide and Conquer
