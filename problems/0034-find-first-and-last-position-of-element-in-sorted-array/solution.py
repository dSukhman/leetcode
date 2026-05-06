class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binary_search(nums, target, find_first):
            left = 0
            right = len(nums) - 1
            index = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    index = mid

                    if find_first:
                        right = mid - 1
                    else:
                        left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return index
        
        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)
        
        return [left, right]
        