class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumsOfValues = defaultdict(int) #initialize set
        sumsOfValues[0] = 1
        runningSum = 0
        count = 0

        for _, num in enumerate(nums):
            runningSum += num

            if runningSum - k in sumsOfValues:
                count += sumsOfValues[runningSum - k]

            sumsOfValues[runningSum] += 1
        
        return count
        #iterate through array
        #have running sum 
        #check if runningSum - k exists in map, 
        #if so thats one subarray of sum k 