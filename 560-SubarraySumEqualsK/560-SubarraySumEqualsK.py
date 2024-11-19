class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = defaultdict(int)
        curSum = 0
        m[0] = 1
        count = 0

        for num in nums:
            curSum += num

            if curSum - k in m:
                count += m[curSum - k]

            m[curSum] += 1
    
        return count
        
