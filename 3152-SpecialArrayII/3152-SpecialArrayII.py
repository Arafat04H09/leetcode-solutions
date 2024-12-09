import re

class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(nums)
        l = [1]
        ans = []
        prefixSum = 1

        for i in range(n - 1):
            if nums[i] % 2 != nums[i + 1] % 2: 
                prefixSum += 1
            
            l.append(prefixSum)
        
        for start, end in queries:
            expectedDiff = abs(end - start)
            if expectedDiff != l[end] - l[start]:
                ans.append(False)
            else:
                ans.append(True)
        
        return ans