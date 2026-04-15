# 0014 — Longest Common Prefix

Difficulty: Easy
Link: https://leetcode.com/problems/longest-common-prefix/

## Approach

Use prefix shrinking to find the longest common prefix.

* Start by assuming the first string is the prefix.
* Compare the prefix with each string in the list.
* While the current string does not start with the prefix, remove the last character from the prefix.
* Continue until all strings share the same prefix.
* Return the remaining prefix after all comparisons.

## Complexity

Time: O(n × m)
Space: O(1)

*(Where n is the number of strings and m is the length of the prefix.)*

## Tags

String
