"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []

        def helper(root):
            if not root:
                return
                
            ans.append(root.val)
            
            for child in root.children:
                helper(child)
            
        helper(root)
        return ans