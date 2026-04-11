class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        if not s: return 0
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        sign = 1
        if s[i] in ['+', '-']:
            sign = -1 if s[i] == '-' else 1
            i += 1
            
        integer = 0

        while i < len(s) and s[i].isdigit():
            integer = int(s[i]) + integer * 10
            if integer * sign <= INT_MIN: return INT_MIN
            if integer * sign >= INT_MAX: return INT_MAX
            i += 1
            
        return integer * sign