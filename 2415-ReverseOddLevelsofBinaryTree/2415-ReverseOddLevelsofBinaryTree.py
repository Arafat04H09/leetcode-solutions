# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfsHelper(left, right, reverse):
            if not left or not right:
                return
            
            if reverse:
                left.val, right.val = right.val, left.val
            
            dfsHelper(left.left, right.right, not reverse)
            dfsHelper(left.right, right.left, not reverse)
        
        dfsHelper(root.left, root.right, True)
        return root