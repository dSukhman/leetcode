# 0023 — Merge k Sorted Lists

Difficulty: Hard
Link: https://leetcode.com/problems/merge-k-sorted-lists/

## Approach

Use divide and conquer to merge multiple sorted linked lists efficiently.

* If the input list is empty, return `None`.
* Repeatedly merge lists in pairs until only one list remains.
* In each iteration, merge adjacent lists using the two-list merge technique.
* Store merged lists in a temporary list.
* Continue until only one fully merged list remains.
* Use a helper function to merge two sorted linked lists.

This method reduces the number of comparisons compared to merging lists one at a time.

## Complexity

Time: O(N log k)

* `N` = total number of nodes
* `k` = number of lists

Space: O(1) (excluding recursion and output)

## Tags

Linked List, Divide and Conquer, Heap, Merge
