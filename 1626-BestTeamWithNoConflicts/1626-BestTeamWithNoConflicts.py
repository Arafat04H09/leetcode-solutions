class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        n = len(scores)
        sortedScores = sorted(zip(ages, scores))
        dp = [0] * n
        dp[0] = sortedScores[0][1]

        for i in range(n):
            olderAge, olderScore = sortedScores[i]
            for j in range(i):
                youngerAge, youngerScore = sortedScores[j]
                
                if olderScore >= youngerScore:
                    dp[i] = max(dp[i], dp[j] + olderScore)
                else:
                    dp[i] = max(dp[i], olderScore) 
        
        return max(dp)
                    


        