class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)

        def dfs(node, parent, visited):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue  
                if neighbor in visited:
                    return [node, neighbor]  
                result = dfs(neighbor, node, visited)
                if result:
                    return result
            return None
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

            visited = set()
            if dfs(node1, -1, visited): 
                return [node1, node2]  

        return []