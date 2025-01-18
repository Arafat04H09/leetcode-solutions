# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def helper(root, minSoFar, maxSoFar):
            if not root:
                return 0 
            
            minSoFar = min(minSoFar, root.val)
            maxSoFar = max(maxSoFar, root.val)

            minLeft = helper(root.left, minSoFar, maxSoFar)
            minRight = helper(root.right, minSoFar, maxSoFar)

            diff = max(abs(maxSoFar - root.val), abs(root.val - minSoFar))

            return max(diff, minLeft, minRight)
        
        return helper(root, root.val, root.val)