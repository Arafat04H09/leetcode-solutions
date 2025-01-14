# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, maxSeenSoFar):
            count = 0
            if root.val >= maxSeenSoFar:
                count += 1
                maxSeenSoFar = max(maxSeenSoFar, root.val)

            if root.left:
                count += dfs(root.left, maxSeenSoFar)
            if root.right:
                count += dfs(root.right, maxSeenSoFar)
            
            return count
        
        return dfs(root, -float("inf"))