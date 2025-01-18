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
        d = defaultdict(int)

        def helper(root):
            if not root:
                return False
            
            target = k - root.val
            if target in d:
                return True
            
            d[root.val] = 1
            
            return helper(root.left) or helper(root.right)
        
        return helper(root)

            