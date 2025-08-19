# Last updated: 8/19/2025, 1:01:46 AM
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
            
        ans = []
        queue = deque([root])

        while queue:
            numNodes = len(queue)

            for i in range(numNodes):
                node = queue.popleft()

                if i  == numNodes - 1:
                    ans.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return ans