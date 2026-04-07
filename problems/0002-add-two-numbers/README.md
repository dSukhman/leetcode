# 0002 — Add Two Numbers

Difficulty: Medium  
Link: https://leetcode.com/problems/add-two-numbers/

## Approach

Use a dummy node to simplify handling the head of the result list.

Traverse both linked lists simultaneously:

- Add corresponding digits from both lists along with the carry.
- Compute the new carry using integer division.
- Create a new node with the digit value (`total % 10`).
- Move to the next nodes in both lists.
- Continue until both lists and carry are exhausted.

Return the next node of the dummy node as the result.

## Complexity

Time: O(max(n, m))  
Space: O(max(n, m))

## Tags

Linked List, Math, Simulation
