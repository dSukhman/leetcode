class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x *= sign
        result = 0
        
        while x:
            digits = x % 10
            if result > (2**31 - 1) // 10: return 0
            x //= 10
            result = result * 10 + digits

        return result * sign
        