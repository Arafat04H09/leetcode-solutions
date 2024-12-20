# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def traverse(node1, node2, isOdd):
            if not node1 or not node2:
                return
            
            if isOdd:
                node1.val, node2.val = node2.val, node1.val
            
            traverse(node1.left, node2.right, not isOdd)
            traverse(node1.right, node2.left, not isOdd)
        
        traverse(root.left, root.right, True)
        return root

        