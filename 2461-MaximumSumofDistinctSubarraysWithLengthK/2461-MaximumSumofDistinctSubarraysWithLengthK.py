class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = set()
        d = defaultdict(int)
        runningSum = 0

        for i in range(k):
            d[nums[i]] += 1
            s.add(nums[i])
            runningSum += nums[i]
        
        maximum = runningSum if len(s) >= k else 0

        for i in range(k, len(nums)):
            d[nums[i - k]] -= 1
            d[nums[i]] += 1
            runningSum -= nums[i - k]
            runningSum += nums[i]

            if d[nums[i - k]] == 0:
                s.remove(nums[i - k])

            if d[nums[i]] == 1:
                s.add(nums[i])

            if len(s) >= k:
                maximum = max(maximum, runningSum)

        return maximum