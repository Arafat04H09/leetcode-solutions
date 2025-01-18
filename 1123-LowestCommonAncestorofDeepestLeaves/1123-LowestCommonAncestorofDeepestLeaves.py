# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def helper(root):
            if not root:
                return 0, root

            d1, left = helper(root.left)
            d2, right = helper(root.right)
            
            if d1 > d2: return d1 + 1, left
            if d2 > d1: return d2 + 1, right

            return d1 + 1, root

        return helper(root)[1] 