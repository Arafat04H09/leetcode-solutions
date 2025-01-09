class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        arr = []

        for i, scores in enumerate(score):
            arr.append((scores[k], i))
        
        arr.sort(reverse = True)

        return [score[index] for _,index in arr]