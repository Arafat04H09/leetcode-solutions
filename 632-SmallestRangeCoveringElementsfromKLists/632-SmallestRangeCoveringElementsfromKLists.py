class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        m = defaultdict(int)
        s = [0] * len(nums)
        sol = [-100001, 100001] 
        nl = []

        for index, array in enumerate(nums):
            for num in array: 
                nl.append((num, index))
        
        nl.sort() 
        start = 0
        
        for end, (num, originalList) in enumerate(nl):
            m[originalList] += 1  
            
            while len(m) == len(nums):
                if num - nl[start][0] < sol[1] - sol[0]:
                    sol = [nl[start][0], num]
                
                m[nl[start][1]] -= 1
                if m[nl[start][1]] == 0:
                    del m[nl[start][1]]
                start += 1

        return sol