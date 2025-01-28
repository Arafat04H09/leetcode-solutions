class Solution(object):
    def twoSum(self, nums, target): 
       # store [value] = index

       # if value in map, then return index

        m = defaultdict(int)

        for index, num in enumerate(nums):
            if target - num in m:
                return (m[target - num], index)
            
            m[num] = index
        
        return -1