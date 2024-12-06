class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        value_map = {num: num for num in nums}

        for oldNumber, newNumber in operations:
            value_map[newNumber] = value_map.pop(oldNumber)

        position_map = {v: k for k, v in value_map.items()}

        for i in range(len(nums)):
            nums[i] = position_map[nums[i]]

        return nums