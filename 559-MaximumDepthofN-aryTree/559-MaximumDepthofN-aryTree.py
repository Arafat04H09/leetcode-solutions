"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        depth = 1
        queue = [root]

        while queue:
            nextQueue = []

            for node in queue:
                for child in node.children:
                    nextQueue.append(child)

            depth += 1
            queue = nextQueue

        return depth - 1