# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
            
        result = [root.val]
        queue = [root]

        while queue:
            nextQueue = []

            for node in queue:
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            
            if nextQueue:
                result.append(nextQueue[-1].val)
            queue = nextQueue
        
        return result


