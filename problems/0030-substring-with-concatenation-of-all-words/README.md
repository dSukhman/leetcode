# 0030 — Substring with Concatenation of All Words

Difficulty: Hard
Link: https://leetcode.com/problems/substring-with-concatenation-of-all-words/

## Approach

Use a sliding window with fixed-size chunks and frequency maps.

* Let each word have the same length `word_len`.
* The total substring length is `word_len * number_of_words`.
* Use a frequency map (`Counter`) to track required words.
* Iterate over possible starting offsets from `0` to `word_len - 1`.
* Slide a window in steps of `word_len`.
* Track seen words using a hashmap.
* If a word appears too many times, shrink the window from the left.
* When the count matches the number of words, record the starting index.
* Reset the window when encountering invalid words.

## Complexity

Time: O(n × word_len)
Space: O(k) — number of unique words

## Tags

Hash Map, Sliding Window, String

## Special Notes

This problem was a bit harder than I expected and I used other solutions to guide my learning.