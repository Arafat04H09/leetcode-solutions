from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(maxsize=10000)
        def aux(m,n):
            if m < 0 or n < 0: return 0
            if m == 1 and n == 1:
                return 1
            return aux(m-1, n) + aux(m, n-1)
        return aux(m,n)