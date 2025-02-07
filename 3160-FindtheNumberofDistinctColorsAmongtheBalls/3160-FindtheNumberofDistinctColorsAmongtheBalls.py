class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        colors = defaultdict(int)
        nodes = defaultdict(int)
        activeColors = 0
        ans = []

        for node, color in queries:
            if nodes[node] > 0: #check if this node had a previous color 
                colors[nodes[node]] -= 1 #decrement that color by 1
                if colors[nodes[node]] == 0: #if its now 0:
                    activeColors -= 1
            
            nodes[node] = color #update color 
            colors[color] += 1
            if colors[color] == 1:
                activeColors += 1

            ans.append(activeColors)
        
        return ans

        