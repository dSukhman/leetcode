# 0018 — 4Sum

Difficulty: Medium
Link: https://leetcode.com/problems/4sum/

## Approach

Use sorting and nested loops combined with the two-pointer technique to find quadruplets that sum to the target.

* Sort the array to allow efficient pointer movement and duplicate handling.
* Use two nested loops to fix the first two numbers.
* Skip duplicate values at both loop levels to avoid repeated quadruplets.
* Use two pointers to search for the remaining two numbers.
* If the total is less than the target, move the left pointer forward.
* If the total is greater than the target, move the right pointer backward.
* If a valid quadruplet is found, add it to the result list and skip duplicates.

## Complexity

Time: O(n³)
Space: O(1) (excluding output)

## Tags

Array, Two Pointers, Sorting
