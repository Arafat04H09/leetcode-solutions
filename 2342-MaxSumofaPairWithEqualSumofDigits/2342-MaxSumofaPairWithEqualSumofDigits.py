class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -1
        m = defaultdict(list)

        for num in nums:
            s = 0
            x = num
            while x > 0:
                s += x % 10 #get digit
                x //= 10 

            if len(m[s]) > 0:
                res =  max(-m[s][0] + num, res)#get the biggest number 
            
            heapq.heappush(m[s], -num) #add number to max heap 
        
        return res 
