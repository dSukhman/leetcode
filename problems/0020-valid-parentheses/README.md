# 0020 — Valid Parentheses

Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/

## Approach

Use a stack to ensure that every opening parenthesis has a matching closing parenthesis in the correct order.

* Create a mapping of closing parentheses to their corresponding opening parentheses.
* Iterate through each character in the string.
* If the character is an opening parenthesis, push it onto the stack.
* If it is a closing parenthesis, check if the stack is empty or if the top element does not match the expected opening parenthesis.
* If a mismatch occurs, return False.
* After processing all characters, return True only if the stack is empty.

## Complexity

Time: O(n)
Space: O(n)

## Tags

Stack, String
