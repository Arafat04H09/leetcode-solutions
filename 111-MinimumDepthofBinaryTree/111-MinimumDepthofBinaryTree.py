# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0 
        
        queue = [root]
        depth = 1

        while queue:
            nextLevel = []

            for node in queue:
                if not node.left and not node.right:
                    return depth

                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)

            queue = nextLevel
            depth += 1

        return depth    
        
        