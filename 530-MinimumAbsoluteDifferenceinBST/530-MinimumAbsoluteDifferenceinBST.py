# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        minDiff = [float("inf")]
        prev = [None]

        def helper(root):
            if not root: 
                return minDiff

            helper(root.left)
            if (prev[0] != None):
                minDiff[0] = min(minDiff[0], root.val - prev[0])

            prev[0] = root.val 
            helper(root.right)
        
        helper(root)
        return minDiff[0]