# 0041 — First Missing Positive

Difficulty: Hard
Link: https://leetcode.com/problems/first-missing-positive/

## Approach

Use cyclic sort to place each positive number in its correct position.

* Iterate through the array.
* While a number is within the valid range `[1, n]`:

  * Swap it into its correct index (`num - 1`).
* After rearranging:

  * Scan the array for the first index where `nums[i] != i + 1`.
* Return the missing positive integer.
* If all positions are correct, return `n + 1`.

This achieves linear time and constant extra space.

## Complexity

Time: O(n)
Space: O(1)

## Tags

Array, Hashing, Cyclic Sort
