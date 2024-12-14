class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = left = 0
        ct = Counter()
        for right, x in enumerate(nums):
            ct[x] += 1
            while max(ct) - min(ct) > 2:
                y = nums[left]
                ct[y] -= 1
                if ct[y] == 0: del ct[y]
                left += 1
            ans += right - left + 1
        return ans