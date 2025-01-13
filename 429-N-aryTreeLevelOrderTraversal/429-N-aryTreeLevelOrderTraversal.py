"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
    
        queue = [root]
        ans = []

        while queue:
            curLevel = []
            nextQueue = []

            for node in queue:
                curLevel.append(node.val)
                for child in node.children:
                    nextQueue.append(child)
            
            ans.append(curLevel)
            queue = nextQueue

        return ans        
        