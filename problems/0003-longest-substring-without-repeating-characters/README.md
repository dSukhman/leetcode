# 0003 — Longest Substring Without Repeating Characters

Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Approach

Use a sliding window with a set to track unique characters.

Traverse the string using two pointers:

* Expand the right pointer to add characters.
* If a duplicate appears, move the left pointer forward and remove characters until the substring is valid.
* Track the maximum length seen during traversal.

## Complexity

Time: O(n)
Space: O(min(n, m))

## Tags

String, Sliding Window, Hash Set
