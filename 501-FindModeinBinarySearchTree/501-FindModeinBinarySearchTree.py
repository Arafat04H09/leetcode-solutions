# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        maxValue = [0]
        d = defaultdict(int)

        def helper(root):
            if not root:
                return
            
            d[root.val] += 1
            if d[root.val] > maxValue[0]:
                maxValue[0] = d[root.val]

            helper(root.right)
            helper(root.left)
        
        helper(root)
        return [key for key in d.keys() if d[key] == maxValue[0]]