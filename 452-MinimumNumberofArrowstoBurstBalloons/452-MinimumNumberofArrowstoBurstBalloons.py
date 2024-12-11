class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        arrows = 1 
        end = points[0][1]

        for x, y in points:
            if x > end:
                arrows += 1
                end = y  
                
        return arrows
