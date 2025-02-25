class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        even = 1  
        odd = 0
        ans = 0
        curr = 0 
        
        for number in arr:
            curr = (curr + number) % 2
            if curr == 0:
                ans += odd  
                even += 1
            else:
                ans += even  
                odd += 1
        
        return ans % 1000000007
