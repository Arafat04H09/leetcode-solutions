class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        results = []
        n = len(nums)
        
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            if all(subarray[j] + 1 == subarray[j + 1] for j in range(k - 1)):
                results.append(max(subarray))
            else:
                results.append(-1)
        
        return results
