# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        d = {}

        def recurse(nodes):
            if nodes == 1:
                return [TreeNode(0)]

            if nodes in d:
                return d[nodes]

            res = []
            for i in range(1, nodes, 2):
                leftTree = recurse(i)
                rightTree = recurse(nodes - i - 1)

                for left in leftTree:
                    for right in rightTree:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        res.append(root)
            
            d[nodes] = res
            return res
        
        return recurse(n)

