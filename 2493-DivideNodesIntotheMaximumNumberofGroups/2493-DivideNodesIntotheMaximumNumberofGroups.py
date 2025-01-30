class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # set up data structures to house graph structure and metrics(?)
        adjacencies = [[] for _ in range(n)]
        parent = [-1] * n
        depth = [0] * n

        for edge in edges:
            adjacencies[edge[0] -1].append(edge[1] - 1)
            adjacencies[edge[1] -1].append(edge[0] - 1)
            self._union(edge[0] - 1, edge[1] - 1, parent, depth)
        
        numGroupsForComponent = {}

        #calculate the maximum number of groups for its component for each node
        for node in range(n):
            numGroups = self.getNumberOfGroups(adjacencies, node, n)

            if numGroups == -1:
                return -1 #invalid split
            rootNode = self._find(node, parent)
            numGroupsForComponent[rootNode] = max((numGroupsForComponent).get(rootNode, 0), numGroups)
        
        return sum(numGroupsForComponent.values())

    def getNumberOfGroups(self, adj_list, src_node, n):
        nodes_queue = deque()
        layer_seen = [-1] * n
        nodes_queue.append(src_node)
        layer_seen[src_node] = 0
        deepest_layer = 0

        # Perform BFS to calculate the number of layers (groups)
        while nodes_queue:
            num_of_nodes_in_layer = len(nodes_queue)
            for _ in range(num_of_nodes_in_layer):
                current_node = nodes_queue.popleft()
                for neighbor in adj_list[current_node]:
                    # If neighbor hasn't been visited, assign it to the next layer
                    if layer_seen[neighbor] == -1:
                        layer_seen[neighbor] = deepest_layer + 1
                        nodes_queue.append(neighbor)
                    else:
                        # If the neighbor is already in the same layer, return -1 (invalid partition)
                        if layer_seen[neighbor] == deepest_layer:
                            return -1
            deepest_layer += 1
        return deepest_layer

    # Find the root of the given node in the Union-Find structure
    def _find(self, node, parent):
        while parent[node] != -1:
            node = parent[node]
        return node

    # Union operation to merge two sets
    def _union(self, node1, node2, parent, depth):
        node1 = self._find(node1, parent)
        node2 = self._find(node2, parent)

        # If both nodes already belong to the same set, no action needed
        if node1 == node2:
            return

        # Union by rank (depth) to keep the tree balanced
        if depth[node1] < depth[node2]:
            node1, node2 = node2, node1
        parent[node2] = node1

        # If the depths are equal, increment the depth of the new root
        if depth[node1] == depth[node2]:
            depth[node1] += 1