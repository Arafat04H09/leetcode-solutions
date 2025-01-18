# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        ans = []

        def helper(root, path):
            if not root:
                return
            
            if not root.left and not root.right:
                ans.append(path + str(root.val))
            
            if root.left:
                helper(root.left, path + str(root.val) + "->")
            if root.right:
                helper(root.right, path + str(root.val) + "->")
        
        helper(root, "")
        return ans