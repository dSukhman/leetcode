# 0028 — Find the Index of the First Occurrence in a String

Difficulty: Easy
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

## Approach

Use a sliding window to check for substring matches.

* Iterate through the `haystack` string.
* At each index, extract a substring of length equal to `needle`.
* Compare the substring with `needle`.
* If a match is found, return the current index.
* If no match is found after checking all positions, return -1.

## Complexity

Time: O(n × m)

* `n` = length of haystack
* `m` = length of needle

Space: O(1)

## Tags

String, Sliding Window
