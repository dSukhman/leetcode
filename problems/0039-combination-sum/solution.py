class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(idx, comb, total):
            if total == target:
                result.append(comb[:])
                return
            
            if total > target or idx >= len(candidates):
                return
            
            comb.append(candidates[idx])
            backtrack(idx, comb, total + candidates[idx])
            comb.pop()
            backtrack(idx+1, comb, total)

        backtrack(0, [], 0)
        return result

        