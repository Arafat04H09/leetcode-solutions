class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        def backtrack(index, curArray, curSum):
            if curSum == target:
                ans.append(curArray[:])
                return
            
            if curSum > target or index >= len(candidates):
                return 
            
            backtrack(index, curArray + [candidates[index]], curSum + candidates[index])            
            backtrack(index + 1, curArray, curSum)
        
        backtrack(0, [], 0)
        return ans