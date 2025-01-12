class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        graph = defaultdict(list)
        inDegree = [0] * n
        
        for src, dest in relations:
            graph[src - 1].append(dest - 1)
            inDegree[dest - 1] += 1
        
        queue = deque()
        minTimes = [0] * n

        for course in range(n):
            if inDegree[course] == 0:
                queue.append(course)
                minTimes[course] = time[course]

        while queue:
            course = queue.popleft()

            for nextCourse in graph[course]:
                inDegree[nextCourse] -= 1
                minTimes[nextCourse] = max(
                    minTimes[nextCourse],
                    minTimes[course] + time[nextCourse]
                )
                if inDegree[nextCourse] == 0:
                    queue.append(nextCourse)
        
        return max(minTimes)

