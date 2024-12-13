class Solution(object):
    def getKth(self, lo, hi, k):
        cache = {1: 1}
        def fn(n):
            if n not in cache:
                if n % 2 == 0:
                    cache[n] = 1 + fn(n / 2)
                else:
                    cache[n] = 1 + fn(3*n + 1)
            return cache[n]
        return sorted((fn(i), i) for i in range(lo, hi+1))[k-1][1]