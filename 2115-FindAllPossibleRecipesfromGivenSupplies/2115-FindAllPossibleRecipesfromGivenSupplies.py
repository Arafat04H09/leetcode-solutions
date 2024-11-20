class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        # graph 
        # inDegrees 

        # for recipes, ingredients 
            # populate the graph indegrees

        # queue 

        # while queue is not empty 
            # go through things in queue and subtract in degree from them
            # check if new indegree is 0 
            # if so append to queue 
        
        #return ans
        graph = defaultdict(list)
        inDegrees = defaultdict(int)

        for rec, ings in zip(recipes, ingredients):
            inDegrees[rec] = len(ings)

            for ing in ings:
                graph[ing].append(rec)
        
        ans = []
        queue = deque(supplies)

        while queue:
            supply = queue.popleft()

            if supply in recipes:
                ans.append(supply)

            for node in graph[supply]:
                inDegrees[node] -= 1

                if inDegrees[node] == 0:
                    queue.append(node)
        
        return ans
