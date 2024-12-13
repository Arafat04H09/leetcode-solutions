class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        score = 0
        heap = [(num, i) for i, num in enumerate(nums)]
        heapify(heap)
        marked = [False] * len(nums)

        while heap:
            num, index = heappop(heap)
            if marked[index] != True:
                print(num)
                score += num
                marked[max(0, index - 1)] = True
                marked[min(len(nums) -1, index + 1)] = True
        
        return score

