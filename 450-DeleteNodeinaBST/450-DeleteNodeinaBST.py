# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                successor = self.findSuccessor(root.right)
                root.val = successor.val
                root.right = self.deleteNode(root.right, root.val)
        return root

    def findSuccessor(self, node):
            while (node.left != None):
                node = node.left
            
            return node