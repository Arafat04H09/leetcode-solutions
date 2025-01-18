# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        graph = defaultdict(list)

        def connect(parent, child):
            if parent and child:
                graph[parent.val].append(child.val)
                graph[child.val].append(parent.val)

            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)
        
        connect(None, root)
        queue = [start]
        seen = set(queue)
        time = -1

        while queue: 
            nextQueue = []
            for node in queue:
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        nextQueue.append(neighbor)
            
            queue = nextQueue
            seen |= set(queue)
            time += 1

        return time