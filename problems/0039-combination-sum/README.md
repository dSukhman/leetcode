# 0039 — Combination Sum

Difficulty: Medium
Link: https://leetcode.com/problems/combination-sum/

## Approach

Use backtracking to generate all possible combinations.

* Recursively build combinations while tracking the current sum.
* Reuse the same candidate by staying at the same index.
* Skip the current candidate by moving to the next index.
* Add combinations to the result when the target sum is reached.
* Stop recursion if the total exceeds the target.

## Complexity

Time: Exponential
Space: O(target)

## Tags

Array, Backtracking, DFS
