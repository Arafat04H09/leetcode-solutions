class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        n = len(nums)
        seen = set(nums)
        
        def dfs(cur):
            if len(cur) == n:
                if cur not in seen:
                    return cur
                return None
            for digit in "01":
                result = dfs(cur + digit)
                if result is not None:
                    return result
            return None
        
        return dfs("")