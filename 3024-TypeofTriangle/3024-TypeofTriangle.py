class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort()
        if nums[-1] >= nums[0] + nums[1]:
            return "none"

        s = set(nums)

        if len(s) == 1:
            return "equilateral"
        elif len(s) == 2:
            return "isosceles"
        else:
            return "scalene"