class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        highest = 0
        substring = set()
        for right, letter in enumerate(s):
            while letter in substring:
                substring.remove(s[left])
                left += 1
            
            substring.add(letter)
            highest = max(highest, len(substring))

        return highest
