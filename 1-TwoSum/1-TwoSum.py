class Solution(object):
    def twoSum(self, nums, target):
        # initialize a map 

        #iterate through nums
            #if #target - num in map 
                # return the old index, new index
            # else
                # put target - num in map 
        
        m = defaultdict(int)

        for i, num in enumerate(nums):
            if target - num in m:
                return (m[target - num], i)
            else:
                m[num] = i
        
        return -1