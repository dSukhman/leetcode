# 0021 — Merge Two Sorted Lists

Difficulty: Easy
Link: https://leetcode.com/problems/merge-two-sorted-lists/

## Approach

Use a dummy node to merge two sorted linked lists efficiently.

* Create a dummy node to act as the start of the merged list.
* Use a pointer to track the current position in the merged list.
* Compare the values of the current nodes in both lists.
* Attach the smaller node to the merged list and move that list forward.
* Move the current pointer forward.
* After one list is exhausted, attach the remaining nodes from the other list.
* Return the merged list starting from the dummy node's next pointer.

## Complexity

Time: O(n + m)
Space: O(1)

## Tags

Linked List, Recursion, Iteration
