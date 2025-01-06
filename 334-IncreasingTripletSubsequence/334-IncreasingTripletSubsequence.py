class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        triplet = [float("inf"), float("inf")]

        for num in nums:
            idx = bisect_left(triplet, num)

            if idx < 2:
                triplet[idx] = num
            else:
                return True

        return False
