# 0040 — Combination Sum II

Difficulty: Medium
Link: https://leetcode.com/problems/combination-sum-ii/

## Approach

Use backtracking with sorting to generate unique combinations.

* Sort the candidates array.
* Recursively build combinations while tracking the current total.
* Skip duplicate values at the same recursion level.
* Since each number can only be used once, move to the next index after selection.
* Stop recursion if the total exceeds the target.
* Add valid combinations to the result when the target is reached.

## Complexity

Time: Exponential
Space: O(target)

## Tags

Array, Backtracking, DFS
