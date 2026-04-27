# 0025 — Reverse Nodes in k-Group

Difficulty: Hard
Link: https://leetcode.com/problems/reverse-nodes-in-k-group/

## Approach

Use recursion to reverse nodes in groups of size `k`.

* First, check whether there are at least `k` nodes remaining in the list.
* If fewer than `k` nodes remain, return the head without reversing.
* Reverse the first `k` nodes using standard linked list reversal logic.
* Recursively call the function on the remaining list.
* Connect the reversed group to the result of the recursive call.
* Return the new head of the reversed group.

This approach ensures that only complete groups of `k` nodes are reversed.

## Complexity

Time: O(n)
Space: O(n/k)

## Tags

Linked List, Recursion
