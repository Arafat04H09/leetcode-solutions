    i = 0
    def bstFromPreorder(self, A, bound=float('inf')):
        if self.i == len(A) or A[self.i] > bound:
            return None
        root = TreeNode(A[self.i])
        self.i += 1
        root.left = self.bstFromPreorder(A, root.val)
        root.right = self.bstFromPreorder(A, bound)
        return root