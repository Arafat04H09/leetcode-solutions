class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -1
        m = defaultdict(lambda: [0, 0])  
        for num in nums:
            s = sum(int(digit) for digit in str(num))
            
            if num > m[s][0]:
                m[s][1] = m[s][0]
                m[s][0] = num
            elif num > m[s][1]:
                m[s][1] = num
            
            if m[s][1] > 0:
                res = max(res, m[s][0] + m[s][1])
        
        return res

