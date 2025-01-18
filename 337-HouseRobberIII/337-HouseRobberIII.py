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
        cache = {}
        def robHelper(root):
            if not root:
                return 0, 0

            if root in cache:
                return cache[root]
            
            dontRob = 0
            rob = root.val

            if root.left:
                dontRob += max(robHelper(root.left))
                rob += max(robHelper(root.left.left))
                rob += max(robHelper(root.left.right))

            if root.right:
                dontRob += max(robHelper(root.right))
                rob += max(robHelper(root.right.left))
                rob += max(robHelper(root.right.right))

            cache[root] = (rob, dontRob)
            return rob, dontRob
        
        return max(robHelper(root))
