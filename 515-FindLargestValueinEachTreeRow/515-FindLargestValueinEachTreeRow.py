# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        rows = defaultdict(lambda: float('-inf'))  

        def dfs(depth, node):
            if not node:
                return 
            
            rows[depth] = max(rows[depth], node.val)
            
            dfs(depth + 1, node.left)
            dfs(depth + 1, node.right)

        dfs(0, root)

        return [rows[depth] for depth in sorted(rows.keys())]

        
        