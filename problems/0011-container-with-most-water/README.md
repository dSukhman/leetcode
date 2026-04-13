# 0011 — Container With Most Water

Difficulty: Medium
Link: https://leetcode.com/problems/container-with-most-water/

## Approach

Use two pointers to maximize the container area.

* Start with two pointers at the beginning and end of the array.
* Calculate the area using the width between pointers and the shorter height.
* Update the maximum area found so far.
* Move the pointer pointing to the shorter height inward, since this may allow a taller boundary.
* Continue until both pointers meet.

## Complexity

Time: O(n)
Space: O(1)

## Tags

Array, Two Pointers, Greedy
