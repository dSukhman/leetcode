# This solution is not optimal, but it is straightforward and easy to understand. It uses a set to store the numbers in the input list, and then iterates through the positive integers starting from 1 until it finds a number that is not in the set. This number is the first missing positive integer.
# The time complexity of this solution is O(n) because we need to iterate through the input list to create the set, and then we may need to iterate through the positive integers until we find the missing one. The space complexity is also O(n) because we need to store the numbers in the set.

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s = set(nums)

        i = 1

        while i in s:
            i += 1

        return i