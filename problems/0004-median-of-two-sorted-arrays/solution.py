class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        len1 = len(nums1)
        len2 = len(nums2)

        left = 0
        right = len1

        while left <= right:
            
            x = (left + right) // 2
            y = (len1 + len2 + 1) // 2 - x

            left1  = float('-inf') if (x == 0)    else nums1[x - 1]
            right1 = float('+inf') if (x == len1) else nums1[x]
            left2  = float('-inf') if (y == 0)    else nums2[y - 1]
            right2 = float('+inf') if (y == len2) else nums2[y]
        
            if left1 <= right2 and left2 <= right1:  
                if (len1 + len2) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                else:
                    return max(left1, left2)

            elif left1 > right2:
                right = x - 1
            else:
                left = x + 1