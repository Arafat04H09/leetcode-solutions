class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        
        diff = defaultdict(list)
        m = float('inf')
        
        for i in range(len(arr) - 1):
            d = arr[i+1] - arr[i]
            m = min(m, d)
            diff[d].append([arr[i], arr[i+1]])
        
        return diff[m]