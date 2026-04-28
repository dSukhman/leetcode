# 0026 — Remove Duplicates from Sorted Array

Difficulty: Easy
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

## Approach

Use the two-pointer technique to remove duplicates in-place.

* If the array is empty, return 0.
* Use a pointer `k` to track the position of the next unique element.
* Iterate through the array starting from index 1.
* If the current element is different from the previous unique element, place it at index `k`.
* Increment `k` to expand the unique portion of the array.
* Return `k`, which represents the number of unique elements.

This ensures duplicates are removed without using extra memory.

## Complexity

Time: O(n)
Space: O(1)

## Tags

Array, Two Pointers
