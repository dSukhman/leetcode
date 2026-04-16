# 0015 — 3Sum

Difficulty: Medium
Link: https://leetcode.com/problems/3sum/

## Approach

Use sorting and the two-pointer technique to find triplets that sum to zero.

* Sort the array to allow efficient duplicate handling and pointer movement.
* Iterate through the array, fixing one number at a time.
* Use two pointers to search for two additional numbers that sum to the negative of the fixed number.
* Skip duplicate values to avoid repeating triplets.
* Add valid triplets to the result list when the sum equals zero.

## Complexity

Time: O(n²)
Space: O(1) (excluding output)

## Tags

Array, Two Pointers, Sorting
