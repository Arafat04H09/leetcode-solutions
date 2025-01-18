class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
            
        graph = defaultdict(list)
        degrees = defaultdict(int)

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

            degrees[node1] += 1
            degrees[node2] += 1
        
        leaves = [node for node in range(n) if degrees[node] == 1]

        while n > 2:
            newLeaves = []

            for leaf in leaves:
                degrees[leaf] -= 1
                n -= 1
                for neighbor in graph[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        newLeaves.append(neighbor)

            leaves = newLeaves

        return leaves