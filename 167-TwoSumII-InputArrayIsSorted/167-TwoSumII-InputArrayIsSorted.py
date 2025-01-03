class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]  

            if s > target:
                r -= 1  
            else:
                l += 1 
        
        return -1
