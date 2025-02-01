class Solution(object):
    def sortByBits(self, arr):
        sol = defaultdict(list)
        arr.sort()
        
        for num in arr:
            bit_count = bin(num).count("1")
            sol[bit_count].append(num)
        
        result = []
        for key in sorted(sol.keys()):
            result.extend(sol[key])
        
        return result