class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        ans = ''

        for idx, s in enumerate(nums):
            ans += '0' if s[idx] == '1' else '1'
        
        return ans