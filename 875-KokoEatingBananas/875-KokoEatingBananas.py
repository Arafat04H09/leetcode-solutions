class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            m = (l + r) // 2  

            total_hours = sum((pile + m - 1) // m for pile in piles)  

            if total_hours <= h:
                r = m  
            else:
                l = m + 1  
        
        return l