# 0024 — Swap Nodes in Pairs

Difficulty: Medium
Link: https://leetcode.com/problems/swap-nodes-in-pairs/

## Approach

Use a dummy node and pointer manipulation to swap nodes in pairs.

* Create a dummy node that points to the head to simplify edge cases.
* Use a `prev` pointer to track the node before the current pair.
* Use a `cur` pointer to track the first node in the pair.
* Identify the second node in the pair.
* Swap the two nodes by adjusting their `next` pointers.
* Move the `prev` pointer to the end of the swapped pair.
* Continue until no more pairs are available.
* Return the list starting from the dummy node's next pointer.

## Complexity

Time: O(n)
Space: O(1)

## Tags

Linked List
