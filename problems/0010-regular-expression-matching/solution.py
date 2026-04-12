class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}

        def regex(i, j):
            # If indicies are already in the memory, return cached result
            if (i, j) in memo:
                return memo[(i, j)]

            # If pattern is complete, string must also be complete
            if j == len(p):
                return i == len(s)

            # Check if current characters match
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            # If next character in pattern is '*', we have two choices:
            if j + 1 < len(p) and p[j + 1] == '*':
                # 1. Skip "x*" entirely and move pattern by 2
                # 2. Use "x*" if match and consume one char from string, stay on same pattern
                result = regex(i, j + 2) or (match and regex(i + 1, j))
            else:
                # Match current character and move both pointers
                result = match and regex(i + 1, j + 1)

            # Store result to avoid recomputation
            memo[(i, j)] = result
            return result
                    
        return regex(0, 0)