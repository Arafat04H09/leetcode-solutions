class Solution(object):
    def maxSum(self, nums, m, k):
        """
        :type nums: List[int]
        :type m: int
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
        
        maximum = runningSum if len(s) >= m else 0

        for i in range(k, len(nums)):
            d[nums[i - k]] -= 1
            d[nums[i]] += 1
            runningSum -= nums[i - k]
            runningSum += nums[i]

            if d[nums[i - k]] == 0:
                s.remove(nums[i - k])

            if d[nums[i]] == 1:
                s.add(nums[i])

            if len(s) >= m:
                maximum = max(maximum, runningSum)

        return maximum