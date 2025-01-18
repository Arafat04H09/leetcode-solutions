# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def robHelper(root):
            if not root:
                return 0, 0

            robLeft = robHelper(root.left)
            robRight = robHelper(root.right)

            rob = root.val + robLeft[1] + robRight[1]
            dontRob = max(robLeft)  + max(robRight)
        
            return rob, dontRob
        
        return max(robHelper(root))