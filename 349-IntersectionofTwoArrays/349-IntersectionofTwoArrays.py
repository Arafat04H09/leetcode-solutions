class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s = set(nums1)
        ans = []
        seen = set()

        for num in nums2:
            if num in s and num not in seen:
                ans.append(num)
                seen.add(num)
        
        return ans