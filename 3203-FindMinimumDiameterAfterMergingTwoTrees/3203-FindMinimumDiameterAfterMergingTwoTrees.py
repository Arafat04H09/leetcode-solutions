class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def farthest(graph: List[List[int]], start: int) -> Tuple[int, int]:
            n = len(graph)
            level = [start]
            seen = [0] * n
            seen[start] = 1
            ans = maxd = -1
            for i in level:
                for j in graph[i]:
                    if seen[j] == 0:
                        seen[j] = seen[i] + 1
                        level.append(j)
                        if seen[j] > maxd:
                            ans = j
                            maxd = seen[j]
            return ans, maxd - 1

        def diameter(edges: List[List[int]]) -> int:
            if not edges:
                return 0
            n = len(edges) + 1
            graph = [[] for _ in range(n)]
            for i, j in edges:
                graph[i].append(j)
                graph[j].append(i)
            node1, _ = farthest(graph, 0)
            node2, d = farthest(graph, node1)
            return d
        
        d1 = diameter(edges1)
        d2 = diameter(edges2)
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)