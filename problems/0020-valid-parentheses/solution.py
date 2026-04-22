class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for paren in s:
            if paren not in mapping:
                stack.append(paren)
            elif paren in mapping.keys():
                if not stack or mapping[paren] != stack.pop():
                    return False

        return not stack

