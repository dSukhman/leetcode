# 0035 — Search Insert Position

Difficulty: Easy
Link: https://leetcode.com/problems/search-insert-position/

## Approach

Use binary search to find the target or its insertion position.

* Initialize two pointers `left` and `right`.
* Perform standard binary search:

  * If the target is found, return its index.
  * If the target is smaller, search the left half.
  * If the target is larger, search the right half.
* When the loop ends, `left` represents the correct insertion index.
* Return `left`.

This works because binary search narrows the valid insertion range.

## Complexity

Time: O(log n)
Space: O(1)

## Tags

Array, Binary Search
