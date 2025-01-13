# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if depth == 1:
            newRoot = TreeNode(val, root)
            return newRoot
        
        curDepth = 1
        queue = [root]

        while queue:
            if curDepth == depth - 1:
                for node in queue:
                    oldLeft = node.left if node.left else None
                    oldRight = node.right if node.right else None

                    newLeft = TreeNode(val, oldLeft)
                    newRight = TreeNode(val, None, oldRight)
                
                    node.left = newLeft
                    node.right = newRight
                return root
            
            nextQueue = []
            for node in queue:
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            
            queue = nextQueue
            curDepth += 1

        return root