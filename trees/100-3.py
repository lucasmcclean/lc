class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False

        if p.val != q.val:
            return False

        if (not p.left and q.left) or (p.left and not q.left):
            return False
        if (not p.right and q.right) or (p.right and not q.right):
            return False

        res = self.isSameTree(p.left, q.left)
        if not res:
            return False

        res = self.isSameTree(p.right, q.right)
        if not res:
            return False

        return True
