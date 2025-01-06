class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        LIS = [1] *  n
        LDS = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    LDS[i] = max(LDS[i], LDS[j] + 1)
        

        minRemovals = float("inf")
        for i in range(1, n - 1):
            if LDS[i] > 1 and LIS[i] > 1:
                minRemovals = min(minRemovals, n - (LIS[i] + LDS[i] - 1))

        return minRemovals