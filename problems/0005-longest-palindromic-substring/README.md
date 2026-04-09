# 0005 — Longest Palindromic Substring

Difficulty: Medium
Link: https://leetcode.com/problems/longest-palindromic-substring/

## Approach

Use the expand around center technique to find palindromes.

For each character in the string:

* Treat the character as the center of a palindrome.
* Expand outward for both odd-length and even-length palindromes.
* Compare the lengths of found palindromes and keep track of the longest one.
* Return the longest palindrome found after checking all centers.

## Complexity

Time: O(n²)
Space: O(1)

## Tags

String, Two Pointers, Dynamic Programming
