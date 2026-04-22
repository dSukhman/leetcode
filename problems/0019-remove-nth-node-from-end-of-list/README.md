# 0019 — Remove Nth Node From End of List

Difficulty: Medium
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

## Approach

Use two pointers to remove the nth node from the end of the list in one pass.

* Initialize two pointers at the head of the list.
* Move the first pointer `n` steps forward.
* If the first pointer reaches `None`, remove the head node.
* Move both pointers forward together until the first pointer reaches the last node.
* The second pointer will be positioned just before the node to remove.
* Update the second pointer's `next` reference to skip the target node.
* Return the head of the updated list.

## Complexity

Time: O(n)
Space: O(1)

## Tags

Linked List, Two Pointers
