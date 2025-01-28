# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        seen = set()

        def helper(node):
            if not node: 
                return False
            
            if k - node.val in seen:
                return True
            
            seen.add(node.val)
            return helper(node.left) or helper(node.right)
        
        return helper(root)