class Solution:
    def maxKDivisibleComponents(self, N: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj_list = defaultdict(list)
        indegrees = [0] * N
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            indegrees[u] += 1
            indegrees[v] += 1
        level = [i for i in range(N) if indegrees[i] <= 1]
        count = 0
        while level:
            nxt_level = set()
            for p in level:
                if values[p] % k == 0:
                    count += 1
                    values[p] = 0
                for nei in adj_list[p]:
                    values[nei] += values[p]
                    indegrees[nei] -= 1
                    if indegrees[nei] == 1:
                        nxt_level.add(nei)
            level = nxt_level
        return count