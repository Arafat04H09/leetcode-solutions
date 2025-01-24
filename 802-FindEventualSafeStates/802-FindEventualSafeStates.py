class Solution(object):
    def eventualSafeNodes(self, g):
        graph = defaultdict(list)
        outDegrees = [0] * len(g)

        for node, neighbors in enumerate(g):
            outDegrees[node] = len(neighbors)
            for neighbor in neighbors:
                graph[neighbor].append(node)
        
        queue = [terminal for terminal in range(len(g)) if outDegrees[terminal] == 0]

        while queue:
            nextQueue = []

            for node in queue:
                for neighbor in graph[node]:
                    outDegrees[neighbor] -= 1
                    if outDegrees[neighbor] == 0:
                        nextQueue.append(neighbor)
            
            queue = nextQueue

        return [terminal for terminal in range(len(g)) if outDegrees[terminal] == 0]
        
        
        