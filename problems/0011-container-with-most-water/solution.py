class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxWater = 0

        while left < right:
            currentWater = (right - left) * min(height[left], height[right])
            maxWater = max(maxWater, currentWater)
            if height[left] <= height[right]:
                left += 1
            else: 
                right -= 1

        return maxWater
        