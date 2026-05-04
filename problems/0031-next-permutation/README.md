# 0031 — Next Permutation

Difficulty: Medium
Link: https://leetcode.com/problems/next-permutation/

## Approach

Use a greedy strategy to find the next lexicographically greater permutation.

* Traverse from right to left to find the first index `i` such that `nums[i] < nums[i + 1]`.
* If such an index exists:

  * Find the smallest element greater than `nums[i]` to the right.
  * Swap them.
* Reverse the subarray to the right of index `i` to get the smallest possible order.
* If no such index exists, reverse the entire array (it is the last permutation).

This ensures the next permutation is the smallest possible larger arrangement.

## Complexity

Time: O(n)
Space: O(1)

## Tags

Array, Greedy
