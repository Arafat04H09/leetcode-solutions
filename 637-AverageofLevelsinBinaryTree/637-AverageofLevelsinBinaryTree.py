# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        queue = [root]
        ans = []

        while queue:
            curLevelSum = 0
            curLevelLength = 0
            nextQueue = []

            for node in queue: 
                curLevelSum += node.val
                curLevelLength += 1

                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            ans.append((float(curLevelSum)/curLevelLength))
            queue = nextQueue

        return ans