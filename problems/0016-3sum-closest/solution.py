class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for j in range(len(nums)):
            i = j + 1
            k = len(nums) - 1

            while i < k:
                total = nums[i] + nums[j] + nums[k]

                if abs(result - target) > abs(total - target): 
                    result = total

                if total < target:
                    i += 1
                
                elif total > target:
                    k -= 1

                else:
                    return target             
        
        return result       