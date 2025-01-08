class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #brute force 
        nums = [1] + nums + [1]
        n = len(nums)
        memo = {}

        def burst(left, right):
            if left > right:
                return 0 
            
            if (left, right) in memo:
                return memo[(left, right)]

            maxCoins = 0

            for i in range(left, right + 1):
                coins = nums[left  - 1] * nums[i] * nums[right + 1]
                coins += burst(left, i - 1) + burst(i + 1, right)
                maxCoins = max(maxCoins, coins)

            memo[(left, right)] = maxCoins
            return maxCoins
        
        return burst(1, len(nums) - 2)