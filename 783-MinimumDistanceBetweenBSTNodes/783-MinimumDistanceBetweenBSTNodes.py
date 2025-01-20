# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        minDiff = [float("inf")]
        prev = [None]

        def helper(node):
            if not node:
                return 
            
            helper(node.left)

            if prev[0] != None:
                minDiff[0] = min(minDiff[0], node.val - prev[0])
            
            prev[0] = node.val
            helper(node.right)
        
        helper(root)
        return minDiff[0]