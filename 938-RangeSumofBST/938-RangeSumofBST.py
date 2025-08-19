# Last updated: 8/19/2025, 1:06:00 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0
        
        left = 0
        right = 0

        if root.val > low:
            left = self.rangeSumBST(root.left, low, high)
        if root.val < high:
            right = self.rangeSumBST(root.right, low, high)

        return root.val + left + right if low <= root.val <= high else left + right
