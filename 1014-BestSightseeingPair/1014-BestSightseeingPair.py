    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = cur = 0
        i = 0
        for j in range(len(A)):
            res = max(res, cur+A[j]+i-j)
            if cur+i -j < A[j]:
                cur = A[j]
                i = j
        return res