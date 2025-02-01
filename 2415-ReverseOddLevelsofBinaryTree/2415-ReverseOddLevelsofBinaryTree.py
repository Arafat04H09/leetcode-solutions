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
        queue = [root]
        reverse = False

        while queue:
            nextQueue = []
            curLevel = []

            for node in queue:
                curLevel.append(node.val)

                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            
            if reverse:
                l = len(curLevel) - 1
                for node in queue:
                    node.val = curLevel[l]
                    l -= 1
            queue = nextQueue
            reverse = not reverse
        
        return root