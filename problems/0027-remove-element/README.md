# 0027 — Remove Element

Difficulty: Easy
Link: https://leetcode.com/problems/remove-element/

## Approach

Use the two-pointer technique to remove all occurrences of a specific value in-place.

* Initialize a pointer `k` to track the position of the next valid element.
* Iterate through the array.
* If the current element is not equal to `val`, place it at index `k`.
* Increment `k` to expand the valid portion of the array.
* Continue until all elements are processed.
* Return `k`, which represents the number of elements not equal to `val`.

This method removes unwanted values without using extra space.

## Complexity

Time: O(n)
Space: O(1)

## Tags

Array, Two Pointers
