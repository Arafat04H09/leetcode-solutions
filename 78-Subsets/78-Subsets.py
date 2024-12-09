class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        def backtrack(tempList, index):
            ans.append(tempList[:])
            
            for i in range(index, len(nums)):
                tempList.append(nums[i])
                backtrack(tempList, i + 1) 
                tempList.pop() 

        backtrack([], 0)
        return ans