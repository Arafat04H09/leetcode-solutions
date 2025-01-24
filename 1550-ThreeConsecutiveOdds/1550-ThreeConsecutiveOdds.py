class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        
        start = 0
        runningSum = sum(arr[:3])

        if arr[2] % 2 == 1 and arr[1] % 2 == 1 and runningSum % 2 == 1: return True

        for end in range(3, len(arr)):
            runningSum -= arr[start]
            runningSum += arr[end]

            if arr[end] % 2 == 1 and arr[end - 1] % 2 == 1 and runningSum % 2 == 1:
                return True
            
            start += 1
        
        return False