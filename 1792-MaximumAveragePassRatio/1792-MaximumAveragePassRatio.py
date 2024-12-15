class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        impacts = []
        for passing, total in classes:
            impact = (passing + 1.0) / (total + 1.0) - passing / float(total)
            impacts.append((-impact, passing, total))  

        heapq.heapify(impacts)  

        while extraStudents > 0:
            negImpact, passing, total = heapq.heappop(impacts)
            passing += 1
            total += 1

            currentRatio = passing / float(total)
            expectedRatio = (passing + 1.0) / (total + 1.0)
            newImpact = -(expectedRatio - currentRatio)

            heapq.heappush(impacts, (newImpact, passing, total))
            extraStudents -= 1

        result = 0
        for _, passing, total in impacts:
            result += passing / float(total)

        return float(result / len(classes))
