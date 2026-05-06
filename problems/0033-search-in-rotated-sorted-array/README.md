# 0033 — Search in Rotated Sorted Array

Difficulty: Medium
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

## Approach

Use binary search with logic to determine which half is sorted.

* Initialize two pointers `low` and `high`.
* While `low <= high`, compute the middle index.
* If the middle element equals the target, return its index.
* Determine which half is sorted:

  * If the left half is sorted:

    * Check if the target lies within this range.
    * If yes, search the left half; otherwise, search the right half.
  * If the right half is sorted:

    * Check if the target lies within this range.
    * If yes, search the right half; otherwise, search the left half.
* If the target is not found, return -1.

## Complexity

Time: O(log n)
Space: O(1)

## Tags

Array, Binary Search
