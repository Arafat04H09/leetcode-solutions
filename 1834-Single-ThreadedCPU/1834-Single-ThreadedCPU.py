class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        tasks = [[enqueueTime, processingTime, i] for i, (enqueueTime, processingTime) in enumerate(tasks)]
        tasks.sort()  
        tasks = deque(tasks)  

        ans = []
        heap = []
        curTime = 0

        while tasks or heap:
            while tasks and tasks[0][0] <= curTime:
                enqueueTime, processingTime, index = tasks.popleft()
                heappush(heap, (processingTime, index))  

            if not heap and tasks:
                curTime = tasks[0][0]
                continue

            processingTime, index = heappop(heap)
            ans.append(index)
            curTime += processingTime  

        return ans


