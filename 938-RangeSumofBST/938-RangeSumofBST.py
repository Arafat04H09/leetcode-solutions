# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        s = [0]

        def helper(node):
            if not node:
                return
            
            if low <= node.val <= high:
                s[0] += node.val
            
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return s[0]
