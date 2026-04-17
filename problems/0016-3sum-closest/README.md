# 0016 — 3Sum Closest

Difficulty: Medium
Link: https://leetcode.com/problems/3sum-closest/

## Approach

Use sorting and the two-pointer technique to find the sum closest to the target.

* Sort the array to allow efficient two-pointer searching.
* Initialize the result using the sum of the first three elements.
* Iterate through the array, fixing one number at a time.
* Use two pointers to calculate the sum of three numbers.
* Update the result whenever a sum closer to the target is found.
* Move pointers based on whether the current sum is less than or greater than the target.
* Return immediately if an exact match is found.

## Complexity

Time: O(n²)
Space: O(1)

## Tags

Array, Two Pointers, Sorting
